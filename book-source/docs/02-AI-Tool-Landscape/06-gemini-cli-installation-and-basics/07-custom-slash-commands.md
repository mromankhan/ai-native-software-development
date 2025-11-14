---
sidebar_position: 7
title: Custom Slash Commands
---

# Custom Slash Commands

**Duration**: 16-18 minutes

> **A Word Before We Begin**
>
> You're doing code reviews. Every single day, you type the same detailed prompt: "Review this code for security vulnerabilities, performance issues, code style..." It's 200+ characters every time. There has to be a better way. In this lesson, you'll see the repetition problem firsthand, then learn how custom slash commands turn that 200-character prompt into 7 keystrokes: `/review`

---

## The Problem: Typing the Same Thing Over and Over

Let's see this in action. You have a code file that needs review:

**File**: `api.py` (payment processing code)
```python
def process_payment(user_id, amount, card_number):
    # Process payment
    query = f"SELECT * FROM users WHERE id = {user_id}"

    # Store card details
    card_data = {
        'number': card_number,
        'amount': amount
    }

    # Log transaction
    print(f"Processing payment: {amount} for user {user_id}")

    return True
```

This code has **obvious security issues** (SQL injection, logging sensitive data, storing card numbers). You need Gemini to review it.

### The Traditional Way: Type the Full Prompt Every Time

To get a thorough review, you need a detailed prompt:

```
Review this code for the following issues:

1. Security vulnerabilities (SQL injection, XSS, authentication bypass, insecure data storage)
2. Performance problems (inefficient algorithms, memory leaks, blocking operations)
3. Code style and maintainability (naming conventions, documentation, error handling)
4. Best practices violations (hardcoded secrets, missing validation, improper logging)

For each issue found, provide:
- Severity: CRITICAL, WARNING, or INFO
- Location: Line number and function name
- Explanation: Why this is a problem
- Recommendation: How to fix it

Focus on production-readiness and security-first mindset.
```

**This is 14 lines, 700+ characters.**

You have to:
1. Type (or copy-paste) this every single time
2. Remember all the criteria you care about
3. Hope you don't forget something important
4. Then paste the code you want reviewed

**If you review 5 files a day, you're typing/pasting this 5 times a day, 25 times a week, 100 times a month.**

### What Happens in Practice

**Reality check**:
- Day 1: You type the full detailed prompt
- Day 2: You copy-paste from yesterday
- Day 3: You shorten it to "review this for security issues"
- Day 4: You forget to check performance
- Day 5: Your teammate uses a different prompt, so reviews are inconsistent

**The problems**:
- ❌ **Repetition**: Same prompt, different day
- ❌ **Inconsistency**: Team members use different criteria
- ❌ **Degradation**: Prompts get shorter and less thorough over time
- ❌ **Lost knowledge**: Good prompts are buried in chat history
- ❌ **Fatigue**: "I'll just skip the detailed review this time..."

---

## The Solution: Custom Slash Commands

What if you could type `/review api.py` and have Gemini automatically use your comprehensive prompt?

**That's what custom slash commands do.**

### Creating Your First Custom Command

Create a file in your home directory:

**Location**: `~/.gemini/commands/review.toml`

**Content**:
```toml
description = "Review code for security, performance, and best practices"
prompt = """
Review this code for:
1. Security vulnerabilities (SQL injection, XSS, auth bypass)
2. Performance issues
3. Code style and maintainability
4. Best practices violations

For each issue:
- Severity: CRITICAL/WARNING/INFO
- Location and explanation
- How to fix it

{'{{args}}'}
"""
```

**What this does**:
1. The `description` appears when you type `/help`
2. The `prompt` is what gets sent to Gemini
3. `{'{{args}}'}` gets replaced with whatever you type after `/review`

### Now the Same Task Becomes Simple

Instead of typing 700 characters, you type **7 characters**:

```
/review api.py
```

**What happens behind the scenes**:
1. Gemini CLI sees `/review`
2. Loads `~/.gemini/commands/review.toml`
3. Replaces `{'{{args}}'}` with `api.py`
4. Sends the full comprehensive prompt to Gemini
5. Gemini reviews your file

**You saved**:
- ⏱️ **Time**: 30 seconds → 2 seconds
- 🧠 **Mental load**: No remembering the full criteria
- ✅ **Consistency**: Same thorough review every time
- 👥 **Team alignment**: Everyone uses the same command

### Team Standardization: Codified Knowledge

When your team creates custom commands:
- **Code reviews are consistent**: Everyone uses `/review` with the same criteria
- **New developers onboard faster**: `/setup` runs your project's specific setup
- **Best practices are encoded**: `/deploy:prod` includes all your safety checks
- **Knowledge doesn't disappear**: Commands live in version control, not chat history

Commands become **team codified knowledge**—your workflows, captured as reusable tools.

#### 💬 AI Colearning Prompt
> "If custom slash commands are just saved prompts, couldn't I just save prompts in a text file and copy-paste them? What's the real advantage of the `/command` approach over copy-paste?"
>
> **Hint**: Think about how `/review` works when you pass a filename vs. copy-pasting both the prompt AND the file content every time.

---

## Seeing the Difference: Before and After

Let's make the transformation concrete with a real example.

### Without Custom Command: The Manual Process

You want to review `api.py`:

**Step 1**: Type or paste your review prompt (14 lines)
**Step 2**: Tell Gemini which file to review

```
Review this code for the following issues:

1. Security vulnerabilities (SQL injection, XSS, authentication bypass, insecure data storage)
2. Performance problems (inefficient algorithms, memory leaks, blocking operations)
3. Code style and maintainability (naming conventions, documentation, error handling)
4. Best practices violations (hardcoded secrets, missing validation, improper logging)

For each issue found, provide:
- Severity: CRITICAL, WARNING, or INFO
- Location: Line number and function name
- Explanation: Why this is a problem
- Recommendation: How to fix it

api.py
```

**Total keystrokes**: ~700 characters (if copy-pasting from a saved file)
**Time**: 15-30 seconds
**Consistency**: Varies (did you remember to paste the latest version of your prompt?)

### With Custom Command: One Line

```
/review api.py
```

**Total keystrokes**: 14 characters
**Time**: 2 seconds
**Consistency**: Always uses the same thorough prompt

**The transformation**:
- 🔒 **700 characters** → **14 characters** (50x reduction)
- 🔒 **30 seconds** → **2 seconds** (15x faster)
- 🔒 **"Did I remember everything?"** → **Always complete and consistent**

### The Real Power: Team Consistency

**Scenario**: Your team of 5 developers does code reviews.

**Without custom commands**:
- Developer A has a detailed 10-point checklist (700 characters)
- Developer B has a shorter 5-point version (300 characters)
- Developer C types it fresh each time (varies)
- Developer D doesn't remember to check security every time
- Developer E joined last week and doesn't have any saved prompt

**Result**: Inconsistent reviews, gaps in coverage, knowledge loss

**With `/review` command** (shared in version control):
- All 5 developers type `/review filename.py`
- All get the same comprehensive review
- New developer E gets instant access to team standards
- Review quality doesn't degrade over time

---

## Part 2: TOML File Structure and Syntax

Custom commands are written in **TOML** format (a simple, readable configuration language like JSON but more human-friendly).

### Required Fields

Every custom command needs two fields:

```toml
description = "Brief description of what this command does"
prompt = """
The actual prompt sent to Gemini.
Can be multi-line.
"""
```

**The `description`**: Shows up when you type `/help` to list all commands
**The `prompt`**: The actual text sent to Gemini when you run the command

### Optional Fields

You can customize behavior:

```toml
description = "Code review assistant"
prompt = "Review this code: {'{{args}}'}"
model = "gemini-2.5-pro"        # Override default model
temperature = 0.7                 # Control creativity (0=deterministic, 1=creative)
systemInstruction = "You are a security expert reviewing code for vulnerabilities"
```

### File Naming Rules

- Filename becomes the command name
- Underscores become hyphens in command names
- Example: `code_review.toml` → `/code_review` or `/code-review`

### Minimal Example

**File**: `~/.gemini/commands/explain.toml`

```toml
description = "Explain a concept in simple terms"
prompt = "Explain {'{{args}}'} in simple terms a 5th grader could understand"
```

**Usage**:
```
/explain quantum computing
```

**Result**: Gemini explains quantum computing at a 5th-grade level.

---

## Part 3: Injection Patterns

The real power comes from **injection patterns**—ways to insert dynamic content into your prompt.

### Pattern 1: Argument Injection (`{'{{args}}'}`)

The `{'{{args}}'}` placeholder gets replaced with whatever you type after the command.

**Example**:
```toml
description = "Review code file for issues"
prompt = "Review this code and suggest improvements:\n{'{{args}}'}"
```

**Usage**:
```
/review src/main.py
```

Becomes:
```
Review this code and suggest improvements:
src/main.py
```

But wait—how does Gemini see the **contents** of `src/main.py`? That's where the next pattern helps.

### Pattern 2: Shell Command Injection (`!{command}`)

The `!{command}` placeholder executes a shell command and injects the output.

**Example**:
```toml
description = "Summarize recent commits"
prompt = """
Summarize these recent commits and identify patterns:

!{git log --oneline -10}

What areas of the codebase are getting the most attention?
"""
```

**Execution**:
1. Runs `git log --oneline -10`
2. Injects the output into the prompt
3. Sends to Gemini

**Output** (what Gemini sees):
```
Summarize these recent commits and identify patterns:

abc1234 Fix authentication bug
def5678 Refactor database queries
ghi9012 Add user profile page
jkl3456 Update dependencies
... (10 commits total)

What areas of the codebase are getting the most attention?
```

### Pattern 3: File Content Injection (`@{filepath}`)

The `@{filepath}` placeholder reads a file and injects its contents.

**Example**:
```toml
description = "Review code against project standards"
prompt = """
Review this code:
@{src/main.py}

Against our team standards:
@{CODING_STANDARDS.md}

Any violations?
"""
```

**Execution**:
1. Reads `src/main.py` and injects content
2. Reads `CODING_STANDARDS.md` and injects content
3. Sends combined prompt to Gemini

This is powerful for keeping prompts in sync with your actual code and standards.

### Pattern 4: Combining All Three

Here's a real-world example using all three injection patterns:

**File**: `~/.gemini/commands/git/commit-message.toml`

```toml
description = "Generate semantic commit message from git diff"
prompt = """
Generate a semantic commit message for these changes:

Staged files:
!{git diff --cached --name-only}

Changes:
!{git diff --cached}

Project conventions:
@{CONTRIBUTING.md}

Focus area: {'{{args}}'}

Format: <type>(<scope>): <description>
Examples: feat(auth): Add OAuth support
"""
```

**Usage**:
```
/git:commit "authentication improvements"
```

**What Happens**:
1. `{'{{args}}'}` → "authentication improvements"
2. `!{git diff --cached --name-only}` → Lists changed files
3. `!{git diff --cached}` → Shows actual diff
4. `@{CONTRIBUTING.md}` → Reads project guidelines
5. Combined prompt goes to Gemini
6. Gemini returns properly formatted commit message

You never typed the diff or read the guidelines—the command handles it.

---

## Part 4: Namespacing and Organization

As your command library grows, you need organization.

### Directory Structure Maps to Namespaces

```
~/.gemini/commands/
├── plan.toml              → /plan
├── review.toml            → /review
├── git/
│   ├── commit.toml        → /git:commit
│   ├── log.toml           → /git:log
│   └── status.toml        → /git:status
├── deploy/
│   ├── staging.toml       → /deploy:staging
│   ├── production.toml    → /deploy:production
│   └── rollback.toml      → /deploy:rollback
└── team/
    └── backend/
        ├── deploy.toml    → /team:backend:deploy
        └── test.toml      → /team:backend:test
```

**Rule**: Directory name becomes namespace. Colons separate namespace levels.

### Best Practices

1. **Group by category**: All git-related commands in `git/`, all deploy commands in `deploy/`
2. **Use namespaces for teams**: `/team:frontend:test`, `/team:backend:deploy`
3. **Global vs Project**:
   - `~/.gemini/commands/` - Personal commands (apply everywhere)
   - `.gemini/commands/` in project root - Project-specific commands
4. **Share with team**: Commit `.gemini/commands/` to version control so everyone benefits

### Project-Level Commands

Create `.gemini/commands/` in your project root for team-specific workflows:

```
my-project/
├── .gemini/
│   └── commands/
│       ├── dev/
│       │   ├── setup.toml      → /dev:setup
│       │   ├── test.toml       → /dev:test
│       │   └── debug.toml      → /dev:debug
│       └── deploy/
│           ├── staging.toml    → /deploy:staging
│           └── prod.toml       → /deploy:prod
```

When developers clone your repo, they get these commands automatically. `/dev:setup` runs your project's specific setup procedure.

---

## Red Flags to Watch

### "Command not found: /review"
- Check file location:
  - `~/.gemini/commands/review.toml` (global)
  - `.gemini/commands/review.toml` (project, if in project root)
- Filename must match exactly (case-sensitive on Linux/Mac, not on Windows)
- Gemini CLI may need restart after adding commands

### "Variable not defined: args"
- You used `{'{{args}}'}` but didn't provide arguments
- Example that fails: `/review` (no file provided)
- Correct: `/review src/main.py`

### "Injection failed: File not found"
- Your `@{filepath}` references a file that doesn't exist
- Check path is correct (relative to current directory or use absolute path)
- Example: `@{STANDARDS.md}` won't work if file is `docs/STANDARDS.md`

### TOML syntax error
- Common mistake: Forgetting quotes around string values
- ✅ Correct: `description = "Review code"`
- ❌ Wrong: `description = Review code`
- Wrong: Trailing commas in multi-line strings

---

## Try With AI

### Prompt 1: Creating Your First Custom Command
```
Help me create a custom Gemini CLI command called /code-review
that takes a file as argument and reviews it for:
1. Security vulnerabilities
2. Performance issues
3. Code style

Show me:
1. The exact TOML file content
2. Where to save it
3. How to use it
4. What output to expect
```

**Expected outcome**: Ready-to-use TOML file you can create.

### Prompt 2: Using All Injection Patterns
```
I want to create a command that:
1. Takes a commit message as argument ({'{{args}}'})
2. Gets the current git status (!{git status})
3. Reads my team's commit guidelines (@{CONTRIBUTING.md})
4. Uses all three injection patterns to verify my commit message is valid

Write the TOML file.
```

**Expected outcome**: Advanced command using all three injection patterns.

### Prompt 3: Project Team Commands
```
My team is [describe: 5 developers / Django project / feature-driven].
Design a set of custom commands using /namespace:command structure that would:
1. Standardize our code review process
2. Automate our deployment checks
3. Help with pull request descriptions
4. Reduce repetitive typing

Show me the directory structure and 3-4 example TOML files.
```

**Expected outcome**: Team command structure aligned to your workflow.

### Prompt 4: Debugging Command Issues
```
I created this custom command but it's not working:

[show your TOML file]

When I run [your command usage], I get this error: [your error message]

Debug this for me. What's wrong? How do I fix it?
```

**Expected outcome**: Specific debugging steps based on your error.
