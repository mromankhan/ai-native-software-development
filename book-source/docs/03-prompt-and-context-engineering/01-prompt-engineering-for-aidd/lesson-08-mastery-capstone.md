---
title: "Lesson 8: Mastery Integration and Capstone — Systematize and Ship"
chapter: 9
lesson: 8
duration_minutes: 40

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment, accreditation alignment, and differentiation
skills:
  - name: "Designing Reusable Prompt Templates"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student drafts 2+ reusable templates that include all 8 AIDD elements"

  - name: "Capstone Planning via QDD"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student uses QDD to elicit 10+ clarifying answers before implementation"

learning_objectives:
  - objective: "Systematize prompt engineering with templates for recurring tasks (feature, bug fix, refactor)"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Templates reviewed for presence of Command, Context, Logic, Role, Formatting, Constraints, Examples, Iterative Questions"

  - objective: "Plan and begin a portfolio-ready capstone using all 8 elements and validation checklist"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Capstone plan includes QDD answers, constraints, validation steps, and initial implementation"

cognitive_load:
  new_concepts: 0
  assessment: "Synthesis only (0 new concepts). Integrates all elements from Lessons 1–7 at B1 ✓"

differentiation:
  extension_for_advanced: "Create organization-wide templates; add CI gates for lint, typecheck, coverage"
  remedial_for_struggling: "Start with one template; use a smaller CLI capstone and expand gradually"
---

## What: Systematizing Prompt Engineering

You’ve learned all eight elements. Now you’ll package them into reusable templates so your future work is faster and more reliable. Templates prevent “forgetting an element,” keep quality consistent, and make collaboration easier.

Common use cases:
- New feature or API endpoint
- Bug fix investigation and patch
- Refactoring for maintainability
- Optimization (performance or memory)
- Test generation and docs updates

## Why: Templates Save Time (and Errors)

Instead of reinventing your prompt each time, use a template that encodes the best practices you’ve already proven: clear command, rich context, explicit logic, constraints, examples, role, formatting, and QDD questions.

## How: Build Prompt Templates (3 examples)

Each template includes all 8 elements: Command, Context (4-layer), Logic, Role, Formatting, Constraints, Examples, Iterative Questions.

### Template 1 — New API Endpoint
```
Command: Implement a new FastAPI endpoint: [path + method].

Context (4-layer):
- Project: [stack, architecture, phase]
- Code: [files, models, related modules]
- Constraints: [versions, security, quality, integration]
- Developer: [experience, preferences, deadline]

Logic (numbered steps):
1) [validation]
2) [business rule]
3) [DB call]
4) [response structure]

Role & Style: Senior Backend Engineer; pragmatic, defensive coding; no bare except; docstrings + type hints.

Formatting: Complete file with imports, Google-style docstrings, type hints, and tests.

Constraints: Python 3.11, FastAPI 0.104.0 (Annotated), SQLAlchemy 2.0, ≥80% coverage.

Examples: Error handling pattern and API response JSON format (provide snippets).

Iterative Questions: Ask 10 questions before coding about auth, data model, edge cases, performance, and testing.
```

### Template 2 — Bug Fix
```
Command: Debug [module.function] failing with [error + context].

Context: include logs, stack trace, minimal repro, related files.

Logic: Diagnose cause → propose fix → implement fix → add regression tests.

Role & Style: Defensive; add error handling and logging consistent with project.

Formatting: Provide diff-style changes plus updated tests.

Constraints: No API changes; maintain backward compatibility; follow style guide.

Examples: Include current error handling snippet and test naming conventions.

Iterative Questions: Ask about environment, versions, recent changes, and data edge cases.
```

### Template 3 — Refactor
```
Command: Refactor [module/function] to reduce complexity and improve readability without changing behavior.

Context: current code, usage sites, performance needs.

Logic: Identify duplication → extract helpers → simplify branches → keep public API stable.

Role & Style: Pragmatic; ensure small, reviewable commits; include docstrings and type hints.

Formatting: Provide complete refactored file and a summary of changes.

Constraints: Maintain tests green; cyclomatic complexity < 10; lint clean.

Examples: Provide a representative class or function from the codebase to mirror style.

Iterative Questions: Ask 10 clarifying questions before refactor.
```

---

## Capstone Project: Portfolio-Worthy Application

Choose one:
- REST API (e.g., feature-rich Task or E-commerce module)
- Data Processor (ETL or analytics pipeline)
- CLI Tool (automation or developer productivity)

Requirements:
- Demonstrate all 8 elements in your prompts
- Use QDD workflow (10+ questions answered)
- Apply the 5-step validation checklist
- Provide working code + tests + docs
- Include at least 2 templates adapted to your project

## Capstone Phase 1: Planning (10 min)

Task: Run QDD to define requirements before building.

Prompt to your AI collaborator:
```
I’m choosing the [REST API | Data Processor | CLI Tool] capstone.

Before proposing an implementation, ask me 10 detailed questions about architecture, security, performance, data model, constraints, and testing. Then, based on my answers, outline a phased plan and initial tasks mapped to my constraints.
```

Success criteria: Clear, answer-backed plan with explicit constraints and a first implementation slice you can start immediately ✓

---

## Capstone Phase 2: Implementation (25 min)

Task: Use your customized templates and all 8 AIDD elements to generate code and tests with your AI collaborator. Apply the 5-step validation checklist to every artifact.

Guidance:
- Drive with a clear Command and Logic steps; keep Constraints active in each prompt.
- Provide Examples (style, API responses, tests) to shape outputs.
- Maintain the Role and Style modifiers for consistency.
- After each AI output: Validate (Read → Secrets → Issues → Test → Compare to Spec) and iterate with targeted fix prompts.

Success criteria: Working code that meets your constraints, passes tests, and aligns with examples ✓

---

## Capstone Phase 3: Documentation (10 min)

Task: Document the project for portfolio use.

Checklist:
- README: problem statement, architecture overview, setup/run steps
- Prompts: include the final versions of your best-performing templates
- Validation: note key issues found and how they were fixed
- “Built with AI” note: explain how AI collaborated and where human validation mattered

Success criteria: Clear, portfolio-ready documentation that showcases your AI-native methodology ✓

---

## Try With AI

Goal: Put templates and QDD into action.

1) Pick one of the three templates above and customize it to your capstone.

2) Run a QDD round using the “ask 10 questions first” pattern. Answer thoroughly.

3) Generate the initial implementation and tests. Apply the 5-step validation checklist.

Outcome: You’ve systematized your prompting, kicked off a capstone with QDD, and validated code like a professional AI collaborator.
