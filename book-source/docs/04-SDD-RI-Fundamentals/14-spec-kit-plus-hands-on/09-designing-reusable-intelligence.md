---
title: "Designing Reusable Intelligence"
chapter: 14
lesson: 9
duration_minutes: 45
proficiency_level: "B1"
cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (When to create skills, Conversation-based skill creation, Skill file structure, Skill vs subagent distinction) at B1 level"
learning_objectives:
  - objective: "Identify recurring patterns that justify creating reusable intelligence"
    bloom_level: "Analyze"
  - objective: "Create a skill through conversation with AI after good sessions"
    bloom_level: "Create"
  - objective: "Determine when to create skill vs subagent based on complexity"
    bloom_level: "Evaluate"
  - objective: "Test and iterate on skills until they work effectively"
    bloom_level: "Apply"
generated_by: "content-implementer v1.0.0"
source_spec: "specs/037-chapter-14-research-paper-pivot/spec.md"
created: "2025-11-26"
last_modified: "2025-11-27"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "4.0.0"
---

# Designing Reusable Intelligence

You've completed the SDD workflow (Lessons 01-08): Constitution → Specify → Clarify → Plan → Tasks → Implement. You wrote specifications, refined requirements, planned architecture, and executed implementation with AI collaboration.

But here's what separates AI-native developers from AI-assisted developers: **The ability to transform good sessions into reusable skills.**

With Skills, you teach your AI specific workflows, tools, and processes. By creating a skill, you're giving your AI a playbook it can reference whenever you need that particular type of help—whether that's writing research sections, validating sources, or refining outlines.

---

## When to Create a Skill

Not every workflow deserves a skill. Create one when you notice:

**After a good session, ask yourself:**
1. **Will I do this again?** (Frequency: 3+ times across projects)
2. **Did it involve multiple decisions?** (Complexity: 5+ decision points)
3. **Would I want the same quality next time?** (Value: consistent results matter)

If 2+ answers are YES → Create a skill.

**Examples from your research paper project:**

| Pattern | Frequency | Complexity | Value | Create Skill? |
|---------|-----------|------------|-------|---------------|
| Writing quality sections | ✅ Every paper | ✅ 6+ decisions | ✅ Consistency | **YES** |
| Validating research sources | ✅ Every source | ✅ 5+ decisions | ✅ Accuracy | **YES** |
| Refining outlines | ✅ Every draft | ✅ 5+ decisions | ✅ Structure | **YES** |
| Formatting citations | ✅ Every source | ❌ 2-3 decisions | ❌ Tool handles | NO |
| Spell checking | ✅ Every draft | ❌ 1 decision | ❌ Automated | NO |

---

## Part A: Creating a Skill Through Conversation

Creating a skill with AI means having a conversation where you explain your approach and share any materials you want included. AI translates this into a properly formatted skill.

### Step 1: Start the Conversation

After a good session (like writing a great section), start a new conversation:

```
I want to create a skill for writing research paper sections.

During our last session, I noticed my best sections had:
- Clear opening that establishes what the section explains
- Evidence integrated naturally, not tacked on
- Logical flow from one paragraph to the next
- Conclusions that connect back to thesis

Can you help me turn this into a reusable skill?
```

**What happens:**
- AI asks clarifying questions about your process
- You explain what makes your approach work
- AI structures this into a skill file

### Step 2: Answer AI's Questions

AI will ask about your process. Provide enough detail that someone capable but unfamiliar could follow your approach.

**Example conversation:**

```
AI: "What makes a section 'good' in your view? How do you know when
     a section is ready vs needs more work?"

You: "A good section has three things:
     1. Every claim is supported by evidence or citation
     2. The opening hooks interest and the ending connects to thesis
     3. Someone unfamiliar with the topic could follow the logic

     It needs more work if I have to re-read sentences to understand them,
     or if claims feel unsupported."

AI: "What's your process for writing a section? Do you outline first,
     write linearly, or iterate?"

You: "I start with a rough outline of key points. Then I write the opening
     paragraph to establish context. Then I fill in evidence for each point.
     Finally I write transitions and the closing. I always read it aloud
     to check flow."

AI: "What quality checks do you apply before considering a section done?"

You: "I check:
     - Does every paragraph have a clear topic sentence?
     - Is every factual claim cited?
     - Does it read smoothly without stopping?
     - Does it connect to the thesis?"
```

### Step 3: AI Builds the Skill File

Based on your conversation, AI creates a complete skill file. Ask:

```
Create the skill file with:
- Metadata (name, description, when to use)
- Process steps from our conversation
- Quality criteria I described
- A usage example
- Self-check validation

Format it as a complete .md file I can save.
```

**AI generates:**

```markdown
# Skill: Section Writing for Research Papers

**Name**: section-writer
**Category**: Research & Academic Writing
**Complexity**: Medium (6 decision points)
**Created**: [date]
**Reusable Across**: Any research paper, thesis, technical documentation

## Description

Guide for writing clear, evidence-supported research paper sections.
Use when writing any section that needs to communicate complex ideas
with proper citations and logical flow.

## When to Use This Skill

- Apply when: Writing sections for research papers
- Apply when: Need consistent quality across multiple sections
- Apply when: Want evidence properly integrated (not tacked on)
- Apply when: Refining sections through iteration
- Skip when: Writing is one-off (low reuse value)
- Skip when: Different context (creative fiction, informal blog)

## Process

### Step 1: Outline Key Points
Before writing, identify 3-5 key points the section must make.
Each point should connect to the thesis.

### Step 2: Write Opening Paragraph
Establish what this section explains and why it matters.
Hook reader interest. Connect to thesis.

### Step 3: Develop Each Point with Evidence
For each key point:
- State the point clearly (topic sentence)
- Provide evidence or citation
- Explain significance (don't let evidence speak for itself)
- Transition to next point

### Step 4: Write Closing
Summarize key insights. Connect back to thesis.
Set up the next section.

### Step 5: Quality Check
Before considering done, verify:
- [ ] Every paragraph has clear topic sentence
- [ ] Every factual claim is cited
- [ ] Section reads smoothly (read aloud test)
- [ ] Section connects to thesis

## Quality Criteria

A section is ready when:
- Someone unfamiliar with topic can follow the logic
- All claims supported by evidence
- No sentences require re-reading to understand
- Opening hooks interest, closing connects to thesis

A section needs more work when:
- Claims feel unsupported
- Reader has to re-read sentences
- Flow feels choppy between paragraphs
- Connection to thesis is unclear

## Usage Example

**Scenario**: Writing Literature Review section on AI in K-12 education

**Invocation**:
```
Use the section-writer skill to write my Literature Review.

Key points to cover:
1. Current state of AI in K-12 education
2. Research on teacher workload reduction
3. Studies on student outcome improvements

Thesis: AI tools can measurably improve K-12 classroom efficiency.
```

**Expected Output**: A structured section with clear opening establishing
context, 3 body segments each with topic sentence + evidence + significance,
smooth transitions, and closing that connects findings to thesis.

## Self-Check Validation

Before considering skill application complete, verify:
- [ ] Opening paragraph hooks interest and establishes context
- [ ] Each key point has topic sentence, evidence, significance
- [ ] Transitions connect paragraphs smoothly
- [ ] Closing summarizes insights and connects to thesis
- [ ] Read-aloud test passes (no awkward sentences)
- [ ] All factual claims have citations
- [ ] Someone unfamiliar could follow the logic
```

### Step 4: Save the Skill File

Create the skills directory and save your skill:

```bash
# Create skills directory (if it doesn't exist)
mkdir -p .claude/skills

# AI saves the skill file
```

Then tell AI:

```
Save this skill to .claude/skills/section-writer.md
```

Your directory structure now includes:

```
my-research-paper/
├── .claude/
│   ├── commands/           # Slash commands from specifyplus init
│   └── skills/             # YOUR reusable intelligence
│       └── section-writer.md
├── .specify/
│   └── memory/
│       └── constitution.md
├── specs/
│   └── [your-paper]/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
└── ...
```

### Step 5: Test the Skill

**Test on a real task:**

```
I need to write the Discussion section for my paper.
Use the section-writer skill to guide me.

Key points:
1. How AI applications address teacher workload
2. Evidence of student outcome improvements
3. Limitations and areas needing more research

Thesis: AI tools can measurably improve K-12 classroom efficiency.
```

**Evaluate the result:**
- Did AI follow the skill's process (outline → opening → evidence → closing)?
- Did output meet the quality criteria (claims cited, flows smoothly)?
- What's missing or needs adjustment?

### Step 6: Iterate Until It Works

If something's off, ask AI to update the skill:

```
The section-writer skill worked well, but I noticed:
- It didn't emphasize checking source credibility
- The quality checklist could be more specific

Update the skill to:
1. Add source credibility check in Step 3
2. Add "minimum 3 sources per major point" to quality criteria

Then save the updated version to .claude/skills/section-writer.md
```

Repeat testing until your skill produces consistent, high-quality results.

---

## Part B: Skill vs Subagent — When to Create Which

As you identify more patterns, you'll wonder: **Should I create a skill or a subagent?**

### Decision Framework

**Create a SKILL (2-6 decision points)** when:
- Human guides the process, AI assists
- You apply the framework, AI helps execute
- Examples: section-writer, outline-refiner, citation-formatter

**Create a SUBAGENT (7+ decision points)** when:
- AI should work autonomously with minimal guidance
- AI makes judgments and returns verdicts
- Pattern requires complex, multi-step reasoning
- Examples: research-validator (evaluates source credibility), fact-checker (verifies claims)

**From your research paper project:**

| Component | Decision Points | Human Involvement | Create |
|-----------|-----------------|-------------------|--------|
| Section writing | 6 | Human guides, AI assists | **SKILL** |
| Outline refinement | 5 | Collaborative iteration | **SKILL** |
| Research validation | 8+ | AI judges credibility | **SUBAGENT** |
| Fact checking | 7+ | AI verifies autonomously | **SUBAGENT** |

### What Makes Subagents Different

A subagent adds three things beyond a skill:

**1. Role Definition** (autonomous identity):
```
**Name**: source-validator
**Autonomy Level**: High (makes accept/reject decisions)
**Invocation**: Automatic (after adding source) or manual
```

**2. Decision Authority** (what it can decide vs escalate):
```
**Can ACCEPT**: Peer-reviewed sources from past 10 years
**Can REJECT**: Non-peer-reviewed sources, outdated sources
**Must ESCALATE**: Borderline cases, conflicting information
```

**3. Reporting Format** (structured output):
```
=== SOURCE VALIDATION ===
Source: [title]
Verdict: [ACCEPT | REJECT | ESCALATE]
Reasoning: [specific criteria applied]
Required Actions: [if any]
```

### Creating a Subagent (Preview)

Subagents follow a similar conversation-based creation process:

```
I want to create a subagent for validating research sources.

The subagent should autonomously:
1. Check if sources are peer-reviewed
2. Evaluate publication date (prefer recent)
3. Assess author credibility
4. Flag potential bias
5. Verify source actually supports the claim being made

It should return a verdict (accept/reject/escalate) with reasoning.

Help me design this subagent with:
- Role definition
- Decision authority (what it can decide vs escalate)
- Reporting format
```

You'll learn more about subagents in later chapters. For now, focus on skills.

---

## Part C: Validating Your Skill Works

Good skills trigger **reasoning mode** (context-specific analysis). Bad skills trigger **prediction mode** (generic responses).

### Test Your Skill's Effectiveness

Ask your AI to apply your skill to a challenging case:

```
Apply the section-writer skill to this vague request:

"Write about AI in education"

Walk me through how you're applying each step of the skill.
Show your reasoning for each quality check.
```

**Good response (reasoning mode):**

```
Applying section-writer skill:

STEP 1 - OUTLINE KEY POINTS:
The request is too vague. Before outlining, I need:
- What specific aspect of AI in education?
- What thesis should this connect to?
- What audience level?

[Skill triggers clarification before proceeding]

STEP 2-4 - [Would proceed after clarification]

QUALITY CHECK:
- Cannot verify "connects to thesis" without knowing thesis
- Cannot ensure "someone unfamiliar can follow" without knowing audience

SKILL VERDICT: Request needs refinement before skill can be applied effectively.
```

**Bad response (prediction mode):**

```
Here's a section about AI in education:

AI is transforming education in many ways. It helps teachers
and students learn better. Many schools are using AI tools...

[Generic content that ignores skill process]
```

If you get prediction mode responses, your skill needs strengthening. Revise with more specific criteria and quality checks.

---

## Part D: Building Your Intelligence Library

### Organizing Your Skills

Standard directory structure:

```
my-research-paper/
├── .claude/
│   ├── commands/                    # Slash commands (from specifyplus)
│   └── skills/                      # YOUR accumulated intelligence
│       ├── section-writer.md        ← Your first skill
│       ├── outline-refiner.md       ← Future skill
│       └── source-evaluator.md      ← Future skill
├── .specify/
│   └── memory/
│       └── constitution.md
├── specs/
└── ...
```

### Intelligence Reuse Strategy

**Skill reuse** (apply to new contexts):

```
# Project 2: Different research paper
I'm writing a section on climate policy impacts.

Apply the section-writer skill from .claude/skills/section-writer.md

Context: This is for a policy paper, not education research.
Key points: (1) Current policy landscape, (2) Economic impacts, (3) Implementation challenges
Thesis: Carbon pricing is the most efficient policy mechanism.
```

**Intelligence composition** (combine multiple skills):

```
# Project 3: Comprehensive paper
Apply these skills in sequence:
1. outline-refiner → improve paper structure
2. section-writer → write each section
3. source-evaluator → validate all citations

Start with outline-refiner on my current outline.
```

---

## Common Mistakes

### Mistake 1: Creating Skills for Trivial Patterns

**The Error**: Creating a skill for "How to format headings"

**Why It's Wrong**: 1-2 decision points don't justify a skill. Save skills for complex, recurring workflows.

**The Fix**: Only create skills for patterns with 5+ decisions that recur across 3+ projects.

### Mistake 2: Skipping the Testing Phase

**The Error**: Saving a skill and assuming it works

**Why It's Wrong**: Skills need iteration. Your first version probably misses edge cases.

**The Fix**: Always test skills on real tasks. Update based on what's missing.

### Mistake 3: Over-Specific Skills

**The Error**: Creating "AI-Education-Literature-Review-Writer" that only works for one topic

**Why It's Wrong**: Intelligence should be reusable. Over-specificity limits value.

**The Fix**: Generalize patterns:
- ❌ "AI-Education-Literature-Review-Writer"
- ✅ "Section-Writer" (works for any research paper section)

### Mistake 4: No Quality Criteria

**The Error**: Skill describes process but not what "good" looks like

**Why It's Wrong**: Without quality criteria, you can't verify output or improve skill.

**The Fix**: Every skill needs explicit quality criteria:
- What makes output "ready"?
- What makes output "needs work"?
- How do you check?

---

## Skill Reuse in Practice

### Project 1: Research Paper (Lessons 04-08)

You execute the complete workflow from scratch:
- Write specification, plan, tasks
- Write sections through trial and error
- Learn what works through iteration
- **Total**: 8-10 hours

### Project 2: New Paper (With `section-writer` Skill)

With your skill, dramatically faster:
1. Write paper specification (30 min)
2. Plan sections (30 min)
3. Write sections using skill guidance (3 hours—skill provides structure)
4. **Total**: 4 hours (50% faster)

### Project 3: Multi-Paper Work (With Multiple Skills)

With accumulated skills:
1. Use `section-writer` skill to write (2 hours)
2. Use `source-evaluator` skill to check citations (1 hour)
3. Use `outline-refiner` skill to improve structure (30 min)
4. **Total**: 3.5 hours

**Intelligence compounds**: Each skill accelerates future work.

---

## Try With AI

Ready to create your first reusable skill? Practice conversation-based skill creation:

**Start Skill Creation:**

> "I want to create a skill for writing research paper sections. During my work on this paper, I noticed my best sections had clear openings, evidence integrated naturally, logical flow, and conclusions connecting to thesis. Help me turn this into a reusable skill. Ask me questions about my process."

**Generate Complete Skill File:**

> "Based on our conversation, create a complete skill file with: metadata (name, category, when to use), process steps, quality criteria, usage example, and self-check validation. Format as a .md file I can save to .claude/skills/section-writer.md"

**Test Your Skill:**

> "Apply the section-writer skill to write my Discussion section. Key points: (1) How AI applications address teacher workload, (2) Evidence of student outcome improvements, (3) Limitations. Walk me through each step of the skill as you apply it."

**Iterate Based on Results:**

> "The skill worked, but I noticed [specific issue]. Update the skill to address this. Save the updated version."

**Decide Skill vs Subagent:**

> "I'm thinking about creating reusable intelligence for validating research sources. Help me decide: (1) How many decision points does this involve? (2) Should human guide or AI work autonomously? (3) Based on that, should this be a skill or subagent? (4) Start the creation process."
