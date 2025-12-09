"""Asset cache for tracking uploaded assets locally.

This prevents re-uploading large assets (images, videos, PDFs) on every sync
by maintaining a local cache of asset hashes.
"""
import json
from pathlib import Path
from typing import Optional, Dict


class AssetCache:
    """Local cache for tracking uploaded asset hashes.

    Stores asset information in .panaversity/asset-cache.json to enable
    incremental asset sync without re-uploading unchanged files.
    """

    def __init__(self, cache_dir: Path = Path(".panaversity")):
        """Initialize asset cache.

        Args:
            cache_dir: Directory to store cache file (default: .panaversity)
        """
        self.cache_dir = cache_dir
        self.cache_file = cache_dir / "asset-cache.json"
        self.cache: Dict[str, Dict] = self._load()

    def _load(self) -> Dict:
        """Load cache from disk."""
        if self.cache_file.exists():
            try:
                return json.loads(self.cache_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                # Corrupted cache, start fresh
                return {}
        return {}

    def _save(self):
        """Save cache to disk."""
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            self.cache_file.write_text(
                json.dumps(self.cache, indent=2),
                encoding="utf-8"
            )
        except OSError as e:
            # Non-fatal: cache is just an optimization
            print(f"Warning: Could not save asset cache: {e}")

    def get(self, book_id: str, storage_path: str) -> Optional[str]:
        """Get cached hash for an asset.

        Args:
            book_id: Book identifier
            storage_path: Storage path of the asset

        Returns:
            Cached hash if exists, None otherwise
        """
        key = f"{book_id}:{storage_path}"
        entry = self.cache.get(key)
        return entry.get("hash") if entry else None

    def set(self, book_id: str, storage_path: str, content_hash: str, size: int):
        """Cache asset info after successful upload.

        Args:
            book_id: Book identifier
            storage_path: Storage path of the asset
            content_hash: SHA256 hash of asset content
            size: Size in bytes
        """
        key = f"{book_id}:{storage_path}"
        self.cache[key] = {
            "hash": content_hash,
            "size": size
        }
        self._save()

    def remove(self, book_id: str, storage_path: str):
        """Remove asset from cache.

        Args:
            book_id: Book identifier
            storage_path: Storage path of the asset
        """
        key = f"{book_id}:{storage_path}"
        if key in self.cache:
            del self.cache[key]
            self._save()

    def clear(self, book_id: Optional[str] = None):
        """Clear cache entries.

        Args:
            book_id: If provided, only clear entries for this book.
                    If None, clear entire cache.
        """
        if book_id is None:
            self.cache = {}
        else:
            # Remove only entries for this book
            prefix = f"{book_id}:"
            self.cache = {
                k: v for k, v in self.cache.items()
                if not k.startswith(prefix)
            }
        self._save()
