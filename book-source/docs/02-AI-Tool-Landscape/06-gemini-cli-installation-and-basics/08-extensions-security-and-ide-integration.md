---
sidebar_position: 8
title: Extensions, Security & IDE Integration
---

# Extensions, Security & IDE Integration

**Duration**: 18-20 minutes

> **A Word Before We Begin**
>
> You've spent hours perfecting your Gemini CLI setup: 3 MCP servers, 5 custom commands, a detailed GEMINI.md file. Now your teammate asks: "How do I get the same setup?" You realize you're about to send them a 15-step instruction document. There has to be a better way. In this lesson, you'll see the team setup problem firsthand, then learn how extensions turn "send 15 instructions" into one command: `gemini extensions install`

---

## The Problem: Sharing Your Setup is Painful

You've built a powerful Gemini CLI setup: MCP servers, custom commands, team context. Now your teammate asks: "How do I get the same setup?"

**The manual way**:
```
STEP 1: Install MCP servers (2 commands)
STEP 2: Configure tool security (edit settings.json)
STEP 3: Download 3 custom command files
STEP 4: Create GEMINI.md with team standards
STEP 5: Set environment variables
```

**The problems**:
- ❌ 15+ manual steps per person
- ❌ Easy to miss steps (wrong directory, missed security config)
- ❌ Version drift (teammates have different versions)
- ❌ Update nightmare (re-send everything when you improve something)

---

## The Solution: Extensions Bundle Everything

What if new teammates could get your **entire setup** with **one command**?

```bash
gemini extensions install https://github.com/myteam/dev-tools-extension
```

**That's what extensions do.**

### What is an Extension?

An **extension** is a **pre-packaged bundle** containing everything:

**Included automatically**:
- ✅ MCP servers (pre-configured with security settings)
- ✅ Custom slash commands (all `.toml` files)
- ✅ Persistent context (GEMINI.md with team standards)
- ✅ Configuration templates
- ✅ Tool filtering rules
- ✅ Environment variable templates
- ✅ Documentation

**MCP server alone**: Single capability (e.g., Playwright)
**Extension (complete package)**: MCP servers + commands + context + security + docs

#### 💬 AI Colearning Prompt
> "If extensions just bundle MCP servers and commands, couldn't we just share a GitHub repo with install instructions? What's the real advantage of the extension format?"
>
> **Hint**: Think about what happens when you update the extension vs. when you update a document with install instructions.

---

## Seeing the Difference: Before and After

**Without Extension**:
- Follow 15-step document (30 minutes)
- Miss a step (wrong directory, no tool filtering)
- Fix issues (another 30 minutes)
- Update available next week → Re-download and replace files

**With Extension**:
```bash
gemini extensions install https://github.com/myteam/dev-tools-extension
```

**What happens**: Everything installs automatically—MCP servers, commands, context, security settings.

**Update**: `gemini extensions update dev-tools-extension`

**The transformation**: 60 minutes → 2 minutes (30x faster), zero errors, always in sync.

---

## Part 1: Extension Development Workflow

### Creating Extensions

You now understand WHY extensions matter. Let's see HOW to create them.

#### Create from Template

```bash
gemini extensions new my-extension mcp-server
```

**Creates**:
```
my-extension/
├── gemini-extension.json   (manifest)
├── GEMINI.md                (persistent context)
├── commands/                (custom slash commands)
│   ├── analyze.toml
│   └── research/
│       └── competitor.toml
└── dist/
    └── server.js            (MCP server code, if included)
```

#### Extension Manifest (`gemini-extension.json`)

```json
{
  "name": "my-extension",
  "version": "1.0.0",
  "description": "Research and analysis tools",
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  },
  "contextFileName": "GEMINI.md",
  "excludeTools": ["run_shell_command"],
  "settings": [
    {
      "name": "API Key",
      "description": "Your API key for the service",
      "envVar": "MY_API_KEY"
    }
  ]
}
```

### Development vs Production Workflow

**Development Mode** (while building):
```bash
gemini extensions link ~/my-extension
```

Changes to your extension's files are **immediately reflected** without reinstalling.

**Use when**:
- Actively developing the extension
- Testing commands and MCP configuration
- Iterating on GEMINI.md content

**Production Mode** (when ready to share):
```bash
gemini extensions install ~/my-extension
gemini extensions install https://github.com/user/my-extension
```

Users must **reinstall** to get updates.

### Managing Extensions

**List installed extensions**:
```bash
gemini extensions list
```

**Enable/disable extensions**:
```bash
gemini extensions disable my-extension
gemini extensions enable my-extension --scope=workspace
```

**Update extensions**:
```bash
gemini extensions update my-extension
gemini extensions update --all
```

**Uninstall extensions**:
```bash
gemini extensions uninstall my-extension
```

### Extension Manifest Structure (Key Fields)

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Extension identifier | `"competitive-research"` |
| `version` | Semantic versioning | `"1.0.0"` |
| `mcpServers` | Included MCP servers | `{ "playwright": {...} }` |
| `contextFileName` | Persistent context file | `"GEMINI.md"` |
| `excludeTools` | Blocked tools (security) | `["run_shell_command"]` |
| `settings` | Configuration required | API keys, etc. |

---

## Part 2: Tool Filtering for Security

### Why Tool Filtering Matters

External MCP servers might have **dangerous capabilities**. A single MCP server might offer:
- `read_file` (safe for analysis)
- `write_file` (risky - could overwrite your code)
- `delete_file` (very dangerous - could destroy files)
- `run_arbitrary_code` (extremely dangerous)

**Without filtering**: Gemini has access to all tools, including dangerous ones.
**With filtering**: You control exactly which tools Gemini can use.

### Two Filtering Approaches

#### Allowlist: `includeTools` (Recommended)

Only allow safe tools:

```json
{
  "mcpServers": {
    "myServer": {
      "command": "python",
      "args": ["server.py"],
      "includeTools": ["read_file", "analyze_data", "generate_report"]
    }
  }
}
```

**Result**: Gemini can ONLY use `read_file`, `analyze_data`, and `generate_report`. All other tools are blocked.

**Strategy**: Start very restrictive, expand only as needed.

#### Blocklist: `excludeTools` (Fallback)

Block dangerous tools only:

```json
{
  "mcpServers": {
    "myServer": {
      "command": "python",
      "args": ["server.py"],
      "excludeTools": ["delete_file", "run_shell_command"]
    }
  }
}
```

**Result**: All tools available EXCEPT `delete_file` and `run_shell_command`.

**Risk**: Might miss dangerous tools you didn't think of.

### Real-World Security Scenario

**Situation**: You want to use an MCP server for code analysis. The server offers these tools:
- `read_file` - Read source code ✅ Safe
- `analyze_code` - Find issues ✅ Safe
- `write_file` - Create fixed versions ⚠️ Risky
- `commit_changes` - Auto-commit to git ❌ Very Dangerous
- `delete_test_files` - Cleanup ⚠️ Risky

**Secure Configuration**:
```json
{
  "mcpServers": {
    "codeAnalyzer": {
      "command": "python",
      "args": ["analyzer.py"],
      "includeTools": ["read_file", "analyze_code"]
    }
  }
}
```

**Result**: Gemini can analyze code but **cannot write or delete files**.

### Best Practices

1. **Understand what tools MCP offers**: Ask Gemini about each server
2. **Use allowlist approach**: Start with safe tools only
3. **Test before enabling**: Verify behavior on non-critical data
4. **Monitor tool usage**: Check what tools Gemini actually uses
5. **Review regularly**: Remove access as needs change

---

## Part 3: IDE Integration

### What IDE Integration Adds

When Gemini CLI connects to your IDE (VS Code), it gains:
- **10 most recent files** (you just edited)
- **Cursor position** (exactly where you're working)
- **Selected text** (the code snippet you're focusing on)
- **Native diff viewer** (review changes before applying)
- **One-click apply** (accept changes in editor)

**Result**: Gemini understands your exact context without you copy-pasting.

### Setup: One Time Only

**Install IDE companion**:
```bash
/ide install
```

Installs the VS Code extension (one-time setup).

### Enable/Disable Per Session

**Enable IDE connection**:
```bash
/ide enable
```

VS Code companion starts connecting. Gemini sees your file context.

**Check status**:
```bash
/ide status
```

**Disable IDE connection**:
```bash
/ide disable
```

Disconnects without uninstalling. You can re-enable anytime.

### VS Code Workflow Example

1. **Working in VS Code** on file `src/main.py`, cursor at line 45
2. **Run in Gemini CLI**:
   ```
   /ide enable
   Review this code and suggest improvements
   ```
3. **What Gemini sees**:
   - 10 recently edited files
   - `src/main.py` (full content)
   - Cursor position (line 45)
   - Selected code (if any)
4. **Gemini responds** with suggestions
5. **Diff viewer opens** in VS Code showing changes
6. **Review** changes side-by-side
7. **Accept with one click** or modify suggestions

### When IDE Integration Adds Value

**Great for**:
- Multi-file code reviews (AI sees all context)
- Large refactoring (no copy-paste needed)
- Complex suggestions (visual diff review)
- Context-aware changes (AI understands your exact location)

**Less useful for**:
- Simple questions (no code context needed)
- Terminal-only workflows (not using VS Code)
- Writing new code from scratch (no reference files)
- Non-VS Code editors (IDE integration is VS Code specific)

---

## Part 4: Choosing the Right Workflow

### Decision Framework

**When to use CLI only** (no IDE, no MCP):
- Simple prompts ("Explain this concept")
- Playing with ideas
- Learning Gemini CLI basics
- No specific code context needed

**When to add MCP servers**:
- Need external capabilities (Playwright, databases, APIs)
- Automating research or analysis
- Accessing constantly updated information
- Business workflows

**When to add IDE integration**:
- Working on existing code (refactoring, reviewing)
- Need visual diff review
- Multi-file changes
- Using VS Code as your editor

**When to bundle as extensions**:
- Team standardization (everyone uses same setup)
- Complex workflows (multiple MCP + commands)
- Repeatable patterns (same setup for all projects)

### Professional Setup Example

A complete setup for a 5-person development team:

**Extension includes**:
- Playwright MCP (competitive research, documentation browsing)
- Context7 MCP (API documentation access)
- Custom `/code-review` command (team code review standards)
- Custom `/plan` command (feature planning)
- GEMINI.md (team conventions, architecture)
- Configured tool filtering (no write/delete access)

**Installation**:
```bash
gemini extensions install https://github.com/myteam/dev-tools-extension
```

**Result**: All 5 team members get consistent setup, standards, and capabilities.

### Real Scenario Walkthrough

**Task**: Review and refactor authentication module

1. **CLI only** (simple question):
   ```
   /ide enable
   Explain JWT token refresh flow in 5 sentences
   ```

2. **Add MCP** (research security patterns):
   ```
   Use Context7 to fetch latest OAuth 2.0 best practices
   ```

3. **Add IDE integration** (refactor code):
   ```
   /ide enable
   Review this authentication module for security and suggest refactoring
   ```
   (VS Code shows diff, review changes, apply)

4. **Use extension** (team adoption):
   ```
   /code-review auth/module.py
   ```
   (Custom command uses team standards from extension)

---

## Red Flags to Watch

### "Extension installation failed"
- Check GitHub URL is correct: `github.com/user/repo`
- Verify extension manifest is valid JSON
- Check network connection

### "Tool not available: write_file"
- Verify `includeTools` configuration is correct
- Check tool name exactly (case-sensitive)
- Try `gemini extensions list` to verify extension loaded

### "IDE connection failed"
- Run `/ide install` to reinstall companion
- Check VS Code is open and focused
- Restart both VS Code and Gemini CLI

### "Security concern: Too much access"
- Review `excludeTools` and `includeTools` configuration
- Test MCP server behavior on dummy data first
- Use allowlist approach (safer than blocklist)
- Ask AI: "What tools can this MCP server access? Which should I block?"

---

## Try With AI

### Prompt 1: Creating an Extension
```
I want to create a Gemini CLI extension for [describe your use case].
The extension should include:
- Which MCP servers? (Playwright, Context7, custom, etc.)
- What custom commands? (What workflows do you want to automate?)
- What persistent context? (What should AI always know about your project?)
- Tool filtering? (Which tools should be restricted?)

Walk me through creating the gemini-extension.json manifest and directory structure.
```

**Expected outcome**: Extension manifest and setup instructions.

### Prompt 2: Security Configuration
```
I'm creating an MCP server that has 12 different tools.
I only need 3 of them: read_file, analyze_code, generate_report.

All others could be risky. Show me:
1. The JSON configuration using includeTools
2. Why allowlist is safer than blocklist
3. What to do if I need a tool I didn't include
```

**Expected outcome**: Secure configuration with security principles explained.

### Prompt 3: IDE Integration Workflow
```
I'm using VS Code and just ran /ide enable.
Design a workflow for reviewing and refactoring a Python file.
Show me:
1. What to type in Gemini CLI
2. What Gemini sees (context from IDE)
3. How the diff viewer helps
4. How to apply changes safely
```

**Expected outcome**: Step-by-step IDE integration workflow.

### Prompt 4: Complete Team Setup
```
I'm setting up Gemini CLI for my team of [X developers / team size].
Our main workflows are [describe: web dev / data analysis / etc].

Design a complete setup including:
1. Which MCP servers would help?
2. What custom commands should we standardize?
3. Should we create an extension?
4. Security configuration?
5. IDE integration strategy?

Give me a checklist we can implement together.
```

**Expected outcome**: Team onboarding strategy with complete setup plan.



