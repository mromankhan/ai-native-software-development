---
title: "Lesson 6: Technical Constraints and Examples — Make AI Code Fit Your Project"
chapter: 9
lesson: 6
duration_minutes: 45

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment, accreditation alignment, and differentiation
skills:
  - name: "Specifying Technical Constraints"
    proficiency_level: "A2→B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student adds 3+ constraints that AI meets in generated code"

  - name: "Providing Style and Pattern Examples"
    proficiency_level: "A2→B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student includes example snippet; AI follows project style and error handling patterns"

learning_objectives:
  - objective: "Constrain AI outputs by versions, security, performance, and integration requirements"
    proficiency_level: "A2→B1"
    bloom_level: "Apply"
    assessment_method: "Exercise adding constraints to a basic prompt; verify outputs satisfy them"

  - objective: "Embed examples (style, API responses, tests) to guide AI toward project-specific code"
    proficiency_level: "A2→B1"
    bloom_level: "Apply"
    assessment_method: "Provide snippet; verify AI matches structure and conventions"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (technical constraints, code examples, integration constraints) fit A2→B1 transition ✓"

differentiation:
  extension_for_advanced: "Combine multiple constraint categories and compare tradeoffs; enforce via CI linters/tests"
  remedial_for_struggling: "Start with version + security only; supply a ready-made style snippet"
---

## What: Technical Constraints in AIDD

Constraints tell your AI collaborator exactly what the code must obey to work in your environment. Categories you’ll use often:

- Dependency constraints (language/framework versions, allowed libraries)
- Performance constraints (latency, memory, throughput)
- Security constraints (validation, rate limiting, crypto, access control)
- Code quality constraints (type hints, coverage, style)
- Integration constraints (existing services, logging, migrations, CI/CD)

These guardrails produce code that fits your project the first time—no costly rewrites later.

## Why: Constraints Ensure Project Fit

Without constraints, AI may choose the newest API, an unsupported version, or a pattern that doesn’t match your stack. With constraints, AI delivers code that compiles, deploys, and integrates on day one. Constraints are not bureaucracy—they’re how you convert “good code” into “our code.”

## How: Specifying Constraints and Using Examples

Start with explicit dependency versions and must/never rules, then add examples to shape style and patterns.

### Dependency Constraints (example)
```
Technical Constraints:
- Python version: 3.11 (use match-case; not Python 3.9 compatible)
- FastAPI version: 0.104.0 (use latest Annotated syntax)
- Database: PostgreSQL 15 with SQLAlchemy 2.0 (new ORM syntax)
- No additional dependencies beyond requirements.txt
- Must run in Docker (Alpine Linux base)
```

### Security and Code Quality Constraints (example)
```
Security Requirements:
- Validate and sanitize all inputs
- Use parameterized queries (no raw SQL)
- Rate limit: 100 requests/min/IP
- Passwords: bcrypt (cost factor 12)
- JWT: 1h access tokens with refresh mechanism
- No sensitive data in logs

Code Quality Standards:
- Type hints required for all functions
- Test coverage ≥ 80% (pytest-cov)
- Follow PEP 8 and Google docstrings
- Cyclomatic complexity < 10 per function
```

### Style Example (guide AI with patterns)
```
Match this error handling pattern:

try:
    result = await some_operation()
except DatabaseError as e:
    logger.error(f"Database error in operation: {str(e)}")
    raise HTTPException(status_code=500, detail="Database error occurred")
except ValidationError as e:
    logger.warning(f"Validation error: {str(e)}")
    raise HTTPException(status_code=400, detail=str(e))
```

### API Response Example (shape outputs)
```
Success Response:
{
  "status": "success",
  "message": "User created successfully"
}

Error Response:
{
  "status": "error",
  "error": {"code": "BAD_REQUEST", "detail": "..."}
}
```

---

## Exercise 1: Add Constraints to a Prompt (10 min)

Task: Start with the basic prompt below. Add at least three constraints (version, security, quality) so the AI output must comply.

Basic prompt:
```
Create a FastAPI endpoint to register a user with email and password.
```

Add constraints (example):
- FastAPI 0.104.0 with Annotated
- Password hashing with bcrypt (cost 12)
- Type hints and Google-style docstrings; tests included

Success criteria: AI’s output meets all specified constraints ✓

---

## Exercise 2: Provide a Style Example (5 min)

Task: Include a short snippet from your project (e.g., error handling or service class pattern). Ask AI to match it when implementing the registration endpoint.

Success criteria: The generated code mirrors your example’s structure and tone ✓

---

## Exercise 3: Combine Constraints + Examples (5 min)

Task: Write a single prompt that includes:
- Command + Context + Logic + Constraints + Example

Outcome target: Production-ready code that fits your stack and patterns.

Success criteria: Output compiles and aligns with your examples and constraints ✓

---

## Try With AI

Goal: See the impact of constraints.

1) Unconstrained run
```
Create a function to connect to a PostgreSQL database and return a connection.
```
Observe: Versions, error handling, and secrets handling may be generic or unsafe.

2) Constrained run
```
Create a Python 3.11 function that returns a SQLAlchemy 2.0 Session for PostgreSQL 15. 
Constraints: No hardcoded secrets; read from environment variables. Add explicit error handling. Include type hints and a docstring. Match this error pattern:

try:
    result = await some_operation()
except DatabaseError as e:
    logger.error(f"Database error in operation: {str(e)}")
    raise HTTPException(status_code=500, detail="Database error occurred")
```

3) Compare
- Which output is safer and closer to your project?
- What constraint had the biggest effect?

Outcome: You practiced turning “good code” into “our code” with explicit guardrails.
