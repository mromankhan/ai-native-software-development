"""FastMCP application instance for PanaversityFS.

This module holds the singleton FastMCP instance that both the server
and all tool modules import. This prevents the double-import issue
when running as `python -m panaversity_fs.server`.

Issue: When running with `-m`, Python loads the main module as `__main__`,
but when tools do `from panaversity_fs.server import mcp`, Python loads
it again as `panaversity_fs.server`, creating two different mcp instances.

Solution: Move the mcp instance to a separate module (this file) that both
server.py and tools import consistently.

Authentication:
- If PANAVERSITY_JWT_SECRET is set: JWT auth is enabled
- If not set: Server runs in dev mode without auth

Lifespan Management:
- Database engine is initialized on startup
- Database engine is properly disposed on shutdown
- Follows MCP SDK best practices for resource lifecycle
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Optional

from mcp.server.fastmcp import FastMCP
from panaversity_fs.config import get_config


@dataclass
class AppContext:
    """Application context with typed dependencies for lifespan management."""
    db_initialized: bool = False


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with proper resource cleanup.

    This context manager:
    1. Initializes the database on startup
    2. Disposes the database engine on shutdown

    Following MCP SDK best practices for resource management.
    """
    from panaversity_fs.database.connection import get_engine, reset_engine, init_db

    # Startup: initialize database
    print("[PanaversityFS] Initializing database connection...")
    try:
        # Ensure tables exist (for dev/test - production uses migrations)
        await init_db()
        print("[PanaversityFS] Database initialized successfully")
        db_initialized = True
    except Exception as e:
        print(f"[PanaversityFS] Database initialization failed: {e}")
        db_initialized = False

    try:
        yield AppContext(db_initialized=db_initialized)
    finally:
        # Shutdown: cleanup resources
        print("[PanaversityFS] Disposing database connections...")
        await reset_engine()
        print("[PanaversityFS] Database connections disposed")


def _create_mcp() -> FastMCP:
    """Create FastMCP instance with optional authentication.

    Returns:
        FastMCP: Configured MCP server instance
    """
    config = get_config()

    # Base configuration
    kwargs = {
        "stateless_http": True,  # Enable Stateless Streamable HTTP (FR-004)
        "json_response": True,   # Disable SSE, use pure JSON responses
        "lifespan": app_lifespan # Proper resource lifecycle management
    }

    # Add authentication if configured
    if config.auth_enabled:
        from panaversity_fs.auth import get_auth_settings
        token_verifier, auth_settings = get_auth_settings()

        if token_verifier:
            kwargs["token_verifier"] = token_verifier
        if auth_settings:
            kwargs["auth"] = auth_settings

        print(f"[PanaversityFS] JWT authentication enabled")
        if config.auth_issuer:
            print(f"[PanaversityFS] Issuer: {config.auth_issuer}")
        print(f"[PanaversityFS] Required scopes: {config.required_scopes}")
    else:
        print("[PanaversityFS] Running in dev mode (no authentication)")

    return FastMCP("panaversity_fs", **kwargs)


# Initialize FastMCP server with stateless HTTP transport
# This singleton is imported by all tool modules
mcp = _create_mcp()
