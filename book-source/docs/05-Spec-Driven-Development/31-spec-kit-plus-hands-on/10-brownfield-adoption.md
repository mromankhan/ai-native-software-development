---
title: "Brownfield Adoption - Adding Spec-Kit Plus to Existing Projects"
chapter: 31
lesson: 10
duration_minutes: 45

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Brownfield Risk Assessment"
    proficiency_level: "B1"
    category: "Strategic"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can evaluate data loss risks before running experimental commands"

learning_objectives:
  - objective: "Identify which files get overwritten vs preserved when running specifyplus init --here"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Document actual file changes with before/after comparison"

  - objective: "Use AI collaboration to merge custom team knowledge with SpecKit Plus template"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully merge CLAUDE.md using /sp.constitution command"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (Brownfield vs greenfield, File overwrite behavior, Experimental status) within B1 limit of 10 ✓"

# Generation metadata
generated_by: "manual-restructure-v5.0.0"
source_spec: "Actual tested behavior of specifyplus init --here command"
created: "2025-11-19"
last_modified: "2025-11-19"
version: "5.0.0"
testing_notes: "Restructured to remove redundant teaching, focus on brownfield-specific behavior only"
---

# Brownfield Adoption - Adding Spec-Kit Plus to Existing Projects

You've learned SpecKit Plus by building new projects (Lessons 1-9). Most real-world work starts differently: existing codebases with custom conventions and team knowledge in files like `CLAUDE.md`.

**The question**: Can you add SpecKit Plus to a project that already exists?

**The answer**: Yes, using `specifyplus init --here`—but it **overwrites CLAUDE.md** completely.

This lesson teaches the actual behavior of `init --here` and how to preserve your team's knowledge during brownfield adoption.

---

## Prerequisites

Before this lesson, you should have completed Lessons 1-9, where you learned:
- ✅ Git safety workflows (branching, backups)
- ✅ Constitution setup and `/sp.constitution` command
- ✅ Working with AI to merge content
- ✅ Creating and managing specs

**This lesson adds ONE new thing**: What's different about brownfield (`init --here` overwrites files).

---

## ⚠️ Experimental Status

**`specifyplus init --here` is EXPERIMENTAL**:
- Official brownfield support in development
- CLAUDE.md gets completely overwritten (not merged)
- Custom commands in `.claude/commands/` preserved
- Requires manual backup before use

---

## Layer 1: Understanding Brownfield Behavior

### What `specifyplus init --here` Does

**Command**:
```bash
specifyplus init --here
```

**Behavior** (tested and verified):

| File/Directory | What Happens |
|---------------|--------------|
| `CLAUDE.md` | ❌ **OVERWRITTEN** - Your 200 lines → SpecKit Plus 240-line template |
| `.claude/commands/` | ✅ **PRESERVED** - Custom slash commands intact |
| `.specify/` | 🆕 **CREATED** - New SpecKit Plus infrastructure |
| `src/`, `tests/` | ✅ **PRESERVED** - All code untouched |
| `README.md` | ✅ **PRESERVED** - Documentation untouched |

### Real Example

**Before `init --here`**:
```
project/
├── CLAUDE.md (33 lines - team's AI instructions)
├── .claude/commands/
│   ├── deploy.md (custom deployment)
│   └── test.md (custom testing)
└── src/ (production code)
```

**After `init --here`**:
```
project/
├── CLAUDE.md (240 lines - SpecKit Plus template) ⚠️ REPLACED
├── .claude/commands/
│   ├── deploy.md (preserved) ✅
│   ├── test.md (preserved) ✅
│   ├── sp.specify.md (new) 🆕
│   └── sp.constitution.md (new) 🆕
├── .specify/ (new SpecKit Plus infrastructure) 🆕
└── src/ (untouched) ✅
```

**Critical observation**: Original CLAUDE.md content is LOST unless backed up.

### Warning Message

```bash
$ specifyplus init --here
Warning: Current directory is not empty (8 items)
Template files will be merged with existing content and may overwrite existing files
Do you want to continue? [y/N]:
```

**"May overwrite"** actually means **"WILL overwrite CLAUDE.md"**.

---

## Layer 2: AI Collaboration - Safe Brownfield Workflow

You already learned safe experimentation workflows in Lessons 1-9. Apply them here:

### Step 1: Create Safety Branch

```bash
# You learned this in Lesson 2
git checkout -b experiment/brownfield-test
```

### Step 2: Test and Observe

```bash
# Run the command
specifyplus init --here
# Type: y

# Observe what changed
git status
git diff CLAUDE.md
```

**What you'll see**: CLAUDE.md completely replaced.

### Step 3: Merge Using AI

**Don't manually edit files.** Use the commands you learned:

```bash
# Work with AI to merge your backup with SpecKit Plus template
claude code
```

**Inside Claude Code**:

```
You: I ran 'specifyplus init --here' and my custom CLAUDE.md was overwritten.
I have a backup with team knowledge about:
- Code standards (Python type hints, docstring style)
- Architecture (FastAPI, PostgreSQL)
- Testing requirements (pytest, 80% coverage)

Help me merge this into the SpecKit Plus structure.

AI: Perfect. Let's use /sp.constitution to add your team standards to the constitution,
and I'll help you identify which parts should stay in CLAUDE.md vs move to constitution.

[AI guides you through categorization and merge]
```

**Key point**: You're using **AI collaboration** (Lesson 2-4 skills), not manual vim editing.

---

## Layer 3: Intelligence Design - Brownfield Adoption Pattern

After successfully adopting SpecKit Plus on 2-3 brownfield projects, you'll notice a pattern. Create a reusable decision framework.

### Create Brownfield Decision Skill

The pattern you've discovered:

**Before running `init --here`, ask**:
1. Does CLAUDE.md have valuable custom content?
2. Is project in git with clean history?
3. Do I have time to merge content after init?

**Create the skill**:

```bash
claude code
> I want to create a skill for deciding when to use brownfield 'init --here' vs greenfield 'init'.

  The pattern I've noticed:
  - Check if CLAUDE.md exists and has custom content
  - Verify git safety net
  - Assess merge effort

  Can you help me create /skill brownfield-adoption-decision?
```

**AI will generate**: `.claude/skills/brownfield-adoption-decision.md` using Persona + Questions + Principles pattern.

**When you'll use this skill**: Every time a client asks "Can we add SpecKit Plus to our existing project?"

---

## Layer 4: Spec-Driven Integration - Client Brownfield Projects

You now have a reusable pattern. Apply it to client projects.

### Decision Framework

**Evaluate the project**:

| Factor | Assessment | Decision |
|--------|-----------|----------|
| **CLAUDE.md content** | 0-50 lines or doesn't exist | ✅ Safe to proceed |
| **CLAUDE.md content** | 50-200 lines custom content | ⚠️ Backup mandatory |
| **CLAUDE.md content** | 200+ lines, months of work | 🛑 Consider manual integration |
| **Git status** | Clean repo, committed | ✅ Safe to proceed |
| **Git status** | No git repository | 🛑 Initialize git first |
| **Custom commands** | Exist in `.claude/commands/` | ✅ Will be preserved |

### Example: Client Scenario

**Client**: "We have a 50,000-line Python API with a custom CLAUDE.md (150 lines). Can we use SpecKit Plus?"

**Your assessment**:
1. **CLAUDE.md**: 150 lines → ⚠️ Backup mandatory
2. **Git**: Has git → ✅ Safe
3. **Decision**: Proceed with brownfield adoption

**Your workflow**:
```bash
# Already learned in Lessons 1-9:
git checkout -b experiment/speckit-plus
# Run brownfield init
specifyplus init --here
# Use AI to merge content (Lesson 2-4 skills)
# Use /sp.constitution for team standards
# Commit result
```

**Client gets**:
- ✅ SpecKit Plus workflow (`/sp.specify`, `/sp.plan`, `/sp.tasks`)
- ✅ Their custom commands preserved
- ✅ Their team knowledge merged into constitution
- ✅ Safe rollback option (experiment branch)

---

## Optional Enhancement: Reverse Engineering

After brownfield adoption, you may want to extract architecture knowledge FROM the codebase itself.

**Command**: `/reverse-engineer src/`

**What it does**:
- Analyzes code to discover architectural patterns
- Generates spec.md from implementation
- Identifies reusable patterns for skills

**When to use**: Large codebases (10k+ lines) with undocumented architecture.

**Full documentation**: [https://github.com/panaversity/ai-native-software-development/blob/main/.claude/commands/reverse-engineer.md](https://github.com/panaversity/ai-native-software-development/blob/main/.claude/commands/reverse-engineer.md)

---

## Summary

**Brownfield adoption = Greenfield workflows + One key difference**

**The difference**: `specifyplus init --here` overwrites CLAUDE.md (everything else preserved).

**Skills you already have** (Lessons 1-9):
- Git safety workflows
- AI-guided merging
- Constitution setup
- Spec-driven development

**New knowledge** (this lesson):
- Which files get overwritten vs preserved
- How to merge using `/sp.constitution`
- When to use brownfield vs greenfield
- Brownfield decision framework pattern

**Next steps**:
1. Practice on test project
2. Create brownfield-adoption-decision skill
3. Apply to client projects

---

## Try With AI

**Prompt 1: Brownfield Assessment**
```
I'm consulting for a client with:
- Existing Python project (20,000 lines)
- Custom CLAUDE.md (80 lines of team standards)
- Git repository with clean history
- 3 custom slash commands

Should they use 'specifyplus init --here' or start fresh?
Walk me through your decision using the brownfield framework.
```

**Prompt 2: Safe Brownfield Workflow**
```
I want to test 'specifyplus init --here' on my existing project.
I have custom CLAUDE.md with team knowledge.

Guide me through:
1. What safety steps to take
2. How to merge my content after init
3. Using /sp.constitution for team standards
```

**Prompt 3: Create Brownfield Skill**
```
Help me create a reusable skill for brownfield adoption decisions.

Pattern I've observed:
- Assess CLAUDE.md value
- Check git safety
- Evaluate merge effort
- Decide: proceed, manual integration, or greenfield

Create /skill brownfield-adoption-decision using Persona + Questions + Principles.
```

---

## Quick Reference

### Files Affected by `init --here`

```bash
# OVERWRITTEN (backup required)
CLAUDE.md

# PRESERVED (safe)
.claude/commands/*.md
src/
tests/
README.md
All other project files

# CREATED (new)
.specify/memory/constitution.md
.specify/templates/
.specify/scripts/
.claude/commands/sp.*.md
```

### Safe Workflow (Lessons 1-9 Skills)

```bash
# 1. Safety branch (Lesson 2)
git checkout -b experiment/brownfield

# 2. Run brownfield init
specifyplus init --here

# 3. Use AI to merge (Lessons 2-4)
claude code
> Help me merge my CLAUDE.md backup with SpecKit Plus using /sp.constitution

# 4. Commit (Lesson 2)
git add -A
git commit -m "feat: brownfield SpecKit Plus adoption"
```

### Decision Checklist

Before running `init --here`:
- [ ] CLAUDE.md backed up (if exists)
- [ ] Git repository clean
- [ ] Understand CLAUDE.md will be overwritten
- [ ] Time allocated to merge content
- [ ] Familiar with `/sp.constitution` command

Only proceed when ALL boxes checked.
