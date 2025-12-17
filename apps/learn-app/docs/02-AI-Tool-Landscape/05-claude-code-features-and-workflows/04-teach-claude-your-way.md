---
title: "Teach Claude Your Way of Working"
sidebar_position: 4
chapter: 5
lesson: 4
duration_minutes: 20

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Conceptual Foundation) → L2 (Hands-On Experience)"
layer_1_foundation: "Understanding skills as encoded expertise, recognizing automatic activation, seeing real-world applications"
layer_2_collaboration: "N/A (preparation for L2 in Lesson 06)"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Skill-Based AI Customization"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can identify repeated procedures in their workflow, understand skill benefits, and experience automatic activation"

learning_objectives:
  - objective: "Understand that skills encode reasoning patterns, not just commands"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Articulate the difference with a concrete example"
  - objective: "Experience skills in action through hands-on practice"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successfully use skills from the Skills Lab"
  - objective: "Identify tasks in your workflow where you repeatedly explain the same preferences"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "List 3 personal tasks with repeated explanation patterns"

# Cognitive load tracking
cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (skills as expertise, automatic activation, procedure mapping, skill creation prep) - well within A2-B1 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Map multiple procedures across different domains; experiment with all 8 skills in the lab"
  remedial_for_struggling: "Focus on the Dr. Claude analogy and hands-on experience first"

# Generation metadata
generated_by: "content-implementer v1.0.0 (043-lesson-04-skills-introduction)"
source_spec: "specs/043-lesson-04-skills-introduction/spec.md"
created: "2025-12-17"
last_modified: "2025-12-17"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "3.0.0"

# Legacy compatibility
prerequisites:
  - "Lessons 01-03: Claude Code installed and working"
  - "Basic experience with Claude Code interactions"
---

# Teach Claude Your Way of Working

You've been using Claude Code for a week. You notice something: you keep explaining the same things.

"When you write code, use TypeScript, not JavaScript. Add comments explaining WHY, not WHAT. Keep functions under 20 lines."

Or maybe it's not code at all: "When you summarize meeting notes, put action items first. Use bullet points, not paragraphs. Highlight decisions in bold."

You might think: "I should save this prompt somewhere and paste it each time."

That instinct is 10% of the answer—and missing 90% of the opportunity.

---

## The One-Time Investment

You've refined your approach over months or years. You know exactly how you want meeting notes structured. You have a system for code reviews that catches real issues. Your blog posts follow a pattern that works.

That expertise lives in your head. Every time you use Claude, you transfer a piece of it through conversation—then it's gone when the session ends.

What if you could capture that expertise once and have it apply automatically, forever?

That's what skills do. Not saving keystrokes—**preserving quality**. You invest once in documenting how you work, and Claude applies that standard consistently across every future session.

---

## What Skills Actually Are

Think about the difference between a general practitioner and a cardiologist.

Both are doctors. Both went to medical school. But when you walk in with chest pain, the cardiologist doesn't start from "what is a heart?" They have years of specialized pattern recognition—which symptoms cluster together, which tests to order first, which treatments work for which patient profiles.

That specialized knowledge is the difference between competent and expert.

**Claude without skills**: A brilliant general practitioner. Knows a lot about everything. Can help with anything. But approaches every task from first principles.

**Claude with skills**: A specialist. When you mention meeting notes, Claude doesn't think "what are meeting notes?" It thinks "action items first, one page max, owners and deadlines for every item"—because that's YOUR procedure, loaded automatically.

**Simple definition**: A skill is encoded expertise. It captures how YOU approach a specific task—the reasoning pattern, the preferences, the quality criteria—so Claude applies it automatically.

**What skills are NOT**: Saved prompts you paste in.

The difference is crucial. You don't invoke a skill by name (though you can). Skills are *discovered automatically*. You just work, and Claude recognizes when your encoded expertise applies.

"Help me write meeting notes from this transcript."

If you have a meeting-notes skill, Claude loads it. Your procedure activates. The output matches your standards—without you mentioning the skill at all.

---

## Hands-On: Experience Skills in Action

Enough theory. Let's feel what skills do.

We've prepared a Skills Lab with 8 ready-to-use skills. Download it and experience automatic skill activation firsthand.

### Step 1: Download the Skills Lab

1. Go to [github.com/panaversity/claude-code-skills-lab](https://github.com/panaversity/claude-code-skills-lab)
2. Click the green **Code** button
3. Select **Download ZIP**
4. Extract the ZIP file
5. Open the extracted folder in your terminal

### Step 2: Try a Skill

Open Claude Code in the skills lab directory:

```bash
claude
```

Then try this prompt:

> "Create a professional project proposal document for a mobile app redesign project. Include executive summary, timeline, and budget sections."

### Step 3: Notice What Happened

You didn't say "use the docx skill." Claude recognized the task and activated the skill automatically.

Try another:

> "Help me write a company newsletter announcing our new AI development initiative. Keep it under 500 words."

Again—automatic activation. The `internal-comms` skill loaded because the task matched.

**Ask Claude directly:**
> "Which skills did you use in our conversation so far? How did you decide when to activate each one?"

This reveals the skill discovery mechanism in action.

### Available Skills in the Lab

| Skill | What It Does |
|-------|--------------|
| `docx` | Create and edit Word documents with formatting |
| `pptx` | Build PowerPoint presentations with layouts |
| `xlsx` | Create spreadsheets with formulas and analysis |
| `pdf` | Extract text, merge PDFs, handle forms |
| `internal-comms` | Templates for newsletters, reports, FAQs |
| `skill-creator` | Guide for building your own skills |

---

## Real Example: The Accountability Buddy

Skills work for any repeated task—not just documents or code.

**The problem:** A developer had a list of personal projects they wanted to complete—learning topics, app ideas, books to read. But weeks passed and nothing got done. They'd tried task trackers before; none stuck.

**The solution:** Instead of another app, they created a skill that turns Claude into an accountability partner.

Here's what the skill does:

```
When user says "check in" or "daily standup":

1. Ask about today's focus (what they planned to work on)
2. Ask what they actually accomplished
3. Ask about blockers or distractions
4. Help set tomorrow's single most important task
5. Log the check-in to a markdown file: logs/YYYY-MM-DD.md
```

**A typical interaction:**

```
User: check in

Claude: Good evening! Let's do your daily check-in.

What was your main focus today?

User: Working on the Python API tutorial

Claude: Got it. What did you accomplish on the Python API tutorial?

User: Finished the authentication section, about 2 hours of work

Claude: Nice progress! Any blockers or distractions?

User: Got sidetracked by email for an hour

Claude: Noted. What's the single most important thing for tomorrow?

User: Complete the database section

Claude: ✅ Check-in logged to logs/2025-12-17.md

Summary:
- Focus: Python API tutorial
- Done: Authentication section (2 hrs)
- Blocker: Email distraction (1 hr)
- Tomorrow: Database section
```

**Why it works:** The skill encodes a specific check-in format that the developer refined over time. The questions are deliberate—"single most important thing" forces prioritization. The log format is consistent, making it easy to review progress over weeks.

**Results:** After two weeks, they'd shipped 10+ micro-projects that had been sitting on their "someday" list for months.

The skill cost 30 minutes to create. It runs automatically whenever they say "check in." The quality is consistent because the procedure is encoded, not improvised each time.

---

## Mapping Your First Procedure

This exercise prepares you for Lesson 06, where you'll create your first skill.

**Step 1: Identify Repetition**

Think about your last week with Claude:
- What did you explain more than once?
- What preferences did you keep restating?
- What quality criteria do you always add?

Write down three tasks where you repeated yourself.

**Step 2: Pick One and Articulate It**

Choose the task with the clearest procedure. Answer:

1. **When does this task come up?**
2. **What steps do you follow?**
3. **What makes the output "yours" vs. generic?**
4. **What would someone need to know to do it your way?**

**Example: Meeting Notes**

> **When**: After any meeting with notes or a transcript
>
> **Steps**: (1) Extract action items with owners and deadlines, (2) Highlight decisions, (3) Summarize discussion points, (4) Flag open questions, (5) Keep to one page
>
> **Distinctive**: Action items FIRST (not buried), one page max, owner names always included
>
> **Implicit knowledge**: People skim notes. Action items are what matter. Nobody reads page 3.

That's a procedure ready for encoding.

---

## Try With AI

**Identify Your Skill Candidates:**

> "I've been using Claude for [describe your work]. Help me identify 3 procedures I repeat that would make good skills. For each one, explain: what the skill would do, when it would activate automatically, and what makes my approach distinctive."

**Prepare Your First Skill:**

> "I want to create a skill for [your task: meeting notes, code review, blog writing, etc.]. Before I write any skill files, help me articulate my procedure. Ask me questions about my steps, preferences, and implicit knowledge. Then document this as a 'procedure specification' I can use when building the actual skill."

---

## Reflection

The shift from "ask Claude each time" to "teach Claude once" mirrors how expertise scales in organizations.

A senior team member doesn't re-explain their approach to every new hire individually. They document it, encode it in processes, make it transferable. The knowledge stops living in one person's head and becomes organizational capability.

Skills do the same for your AI partnership. Your procedures—refined over years—become persistent, portable, automatic.

The question isn't whether you have procedures worth encoding. You do.

The question is which one you'll encode first.
