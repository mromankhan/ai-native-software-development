---
title: "Lesson 7: Question-Driven Development (QDD) and Roleplay — Get Expert, Tailored Code"
chapter: 9
lesson: 7
duration_minutes: 50

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment, accreditation alignment, and differentiation
skills:
  - name: "Practicing QDD (Iterative Clarifying Questions)"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student prompts AI to ask 10 questions before complex implementation; answers produce better code"

  - name: "Adopting Specialized AI Roles"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student sets role (e.g., Senior Backend Engineer) and style modifiers; receives domain-grade responses"

learning_objectives:
  - objective: "Use QDD to replace guesswork with targeted clarifying questions before coding"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "AI asks ≥10 relevant questions; final output reflects answers"

  - objective: "Guide AI with specialized roles and style modifiers for higher-quality implementations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Roleplay prompt yields expert, pragmatic code with defensive practices"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (QDD workflow, AI roleplay, AI as consultant) match CEFR B1 ✓"

differentiation:
  extension_for_advanced: "Chain QDD rounds (architecture → testing → observability); compare outputs across roles"
  remedial_for_struggling: "Provide a question bank starter; use a simpler feature (e.g., notes API)"
---

## What: Question-Driven Development (QDD)

QDD is the most powerful AIDD technique for complex tasks. Instead of the AI guessing your requirements, you explicitly ask it to question you first—then it generates code tailored to your answers.

Why it works: AI excels at structured inquiry. Ten minutes answering good questions can save hours of debugging a misaligned solution.

## Why: QDD Produces Better Code

Without QDD → generic patterns, wrong assumptions, mismatched integrations.
With QDD → specificity about auth method, data model, error handling, testing, performance, and deployment—before code is generated.

## How: The QDD Process

Follow these four steps (use the authentication example from your context):

1) Initial Prompt with Question Request
```
I need to implement a user authentication system for a FastAPI application.

Before you provide an implementation, ask me 10 detailed technical questions that will help you create the most appropriate solution for my specific needs.
```

2) AI Asks Clarifying Questions
Expect questions about JWT vs OAuth2, DB/ORM, RBAC, token lifetimes, email verification, rate limiting, testing strategy, etc.

3) Provide Detailed Answers
Answer concretely (e.g., PostgreSQL 15 + SQLAlchemy 2.0, JWT with refresh tokens, RBAC roles, coverage goals).

4) AI Generates Tailored Solution
Now the implementation fits your decisions instead of a generic tutorial.

### Advanced QDD Types

- Architecture Review Questions: scalability, security, performance, maintainability, missing features; “Be specific about which files or functions.”
- Debugging Question Process: environment, traffic, connection settings, monitoring, recent changes; ask in priority order.
- Optimization Questions: workload, metrics, caching, expected patterns.

## Roleplay: Specialized Technical Expertise

Switch from “generic developer” to a focused expert. Example roles:

- Senior Backend Engineer (Python/FastAPI, auth, DB optimization, microservices)
- Expert Frontend Developer (React/TypeScript, accessibility, performance)
- DevOps Engineer (Docker/K8s, CI/CD, Terraform)
- Data Scientist (pandas/sklearn/TensorFlow, MLOps)

Style modifiers:
```
Be pragmatic; prioritize working, maintainable code. 
Write defensive code for edge cases and errors.
Make it work, make it right, make it fast.
Avoid common anti-patterns (no bare except, no mutable defaults, use context managers, avoid global state).
```

---

## Exercise 1: Practice QDD Workflow (20 min)

Task: Choose a complex feature (e.g., payment processing). Ask the AI to interview you first with 10+ questions. Answer them, then request the implementation.

Success criteria: AI’s final code clearly reflects your answers (auth method, data schema, error handling, tests, constraints) ✓

---

## Exercise 2: Adopt a Specialized Role (10 min)

Task: Create a roleplay prompt for a senior backend engineer with FastAPI expertise and defensive coding style. Use it to implement a secure refresh-token endpoint.

Success criteria: Output shows security best practices, error handling, and matches style modifiers ✓

---

## Try With AI

Goal: Experience QDD vs. direct implementation.

1) QDD approach for a Task Management REST API
```
I need to implement a Task Management REST API (tasks CRUD, auth, pagination).

Before writing any code, ask me 10 detailed questions to tailor the solution to my needs. Cover auth strategy, data model, validation, error handling, performance, and testing. After I answer, propose an implementation plan and then generate the code.
```

2) Direct approach (for comparison)
```
Create a FastAPI REST API for task management with CRUD endpoints.
```

3) Compare
- Which path produced code closer to your needs?
- Which required fewer follow-up fixes?

Outcome: You practiced the interview-first collaboration that unlocks expert, tailored code from the AI.
