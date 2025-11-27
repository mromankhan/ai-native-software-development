---
title: "What Is an AI Agent?"
sidebar_position: 1
description: "Define AI agents using Google's authoritative framework, understand the 5-Level Taxonomy, and discover the paradigm shift from bricklayer to director."
proficiency_level: B1
estimated_time: 35
learning_objectives:
  - "Define AI agents using the paper's definition and explain its components"
  - "Classify systems (LLMs, tools, agents) using the 5-Level Taxonomy (Level 0-4)"
  - "Articulate the paradigm shift from 'bricklayer' (traditional development) to 'director' (agent development)"
skills:
  agent_terminology:
    proficiency: B1
  system_classification:
    proficiency: B1
generated_by: content-implementer v1.0.0
source_spec: specs/038-chapter-33-intro-ai-agents/spec.md
created: 2025-11-27
last_modified: 2025-11-27
version: 1.0.0
---

# What Is an AI Agent?

You've spent the last five months becoming proficient with Claude Code—learning prompts, specifications, Python, testing, and how to collaborate with AI on complex projects. Claude Code is powerful because it reasons about problems, suggests solutions, and refines work based on your feedback. But Claude Code is fundamentally a *collaborator*—it responds to your requests, it doesn't autonomously decide what to do next.

Starting in 2025, AI development is shifting. The systems being built are moving from *assistant* (responds to requests) to *agent* (perceives situations, makes decisions, takes action independently). This shift changes what you'll build, how teams coordinate, and what skills are most valuable.

This lesson establishes the mental models you need to understand that shift. By the end, you'll be able to define what makes a system an agent, classify systems using a clear taxonomy, and understand why agent development is becoming a core skill.

## Why Understanding Agents Matters Now

The statistics tell a story about where the industry is moving:

**Today's Landscape**:
- **800+ million people** use ChatGPT weekly, yet the vast majority interact with it as a chatbot (query-response, no autonomy) [OpenAI, 2025]
- **90%+ of developers** now use AI coding assistants daily, but mostly as code generation tools (describe problem, get code) [GitHub Copilot survey, 2024]

**The Emerging Frontier**:
- **44% of US work hours** could potentially involve tasks suitable for AI agent automation by 2030 (McKinsey)—work that requires autonomous reasoning and decision-making, not just generation
- **$2.9 trillion economic value potential** from agent automation by 2030 (McKinsey)
- **7x growth** in AI fluency demand (fastest-growing skill category in the labor market)

The gap between "AI assists humans" (current state) and "AI acts autonomously in defined domains" (emerging state) is where new value concentrates. Developers who learn agent patterns in 2025 will build systems in 2026-2027 that seem impossible today.

## What Is an AI Agent?

The clearest definition comes from Google's "Introduction to Agents" whitepaper (November 2025):

> "The combination of models, tools, an orchestration layer, and runtime services which uses the LM in a loop to accomplish a goal"

This definition contains the essential components. Let's unpack each:

**Model** ("Brain"): The reasoning engine—typically an LLM like Claude, GPT-4, or Gemini—that processes information, understands context, and makes decisions about next steps.

**Tools** ("Hands"): Mechanisms that connect the model to the outside world. These could be APIs (fetch current weather), databases (search documents), code execution environments, or functions that perform specific actions. Without tools, the model can only reason; it can't act.

**Orchestration Layer** ("Nervous System"): The governing logic that coordinates the reasoning process. This includes planning strategies (breaking complex problems into steps), memory management (both short-term context and long-term knowledge), and decision-making about when to think longer, call a tool, or ask a human. The orchestration layer is what distinguishes agents from simple tool-calling LLMs.

**Runtime Services** ("Body"): The deployment infrastructure that makes the agent accessible—hosting, APIs, monitoring, logging. This is what makes the agent operational and observable.

**The Loop**: What ties everything together is the *loop*. The model doesn't make one decision and stop. It reasons, takes action, observes the result, and reasons again. This feedback loop is what enables agents to handle complex, multi-step problems that would be difficult for a single LLM call.

**Example**: Think about Claude Code analyzing your codebase. It reads files, identifies issues, proposes changes, observes your feedback, and refines its suggestions. That's not a single question-answer cycle—it's a loop. The loop is what makes it feel intelligent.

---

## The 5-Level Taxonomy: From LLM to Autonomous System

Not every AI system is an agent, and not all agents are equally autonomous. The paper provides a clear taxonomy for classifying systems based on their capabilities:

### Level 0: Core Reasoning System

A pure LLM with no tools, no planning, no loop. Users ask questions; the LLM generates responses. This includes ChatGPT in its simplest form—powerful for conversation and explanation, but unable to take action in the world or access real-time information.

**Capability**: Generation only (no action)

**Example**: ChatGPT answering "Explain what machine learning is"

---

### Level 1: Connected Problem-Solver

An LLM equipped with tools for accessing real-time information and taking basic actions. The model can call functions, query APIs, or execute code, but the reasoning is relatively straightforward—typically a single reasoning pass with tool calls.

**Capability**: Access external data and execute basic actions based on a single reasoning step

**Example**: ChatGPT with plugins that can check current weather, look up stock prices, or search the web. Claude Code with the ability to run test suites and observe results.

---

### Level 2: Strategic Problem-Solver

An LLM with context engineering—the ability to actively select, package, and manage the most relevant information for each step of its plan. This level includes multi-step planning, where the agent reasons about what it needs to accomplish, breaks down the problem, and executes steps sequentially while adapting based on observations.

**Capability**: Multi-step planning with context optimization

**Example**: Claude Code executing a full development workflow—analyzing requirements, designing architecture, implementing in stages, testing, and refining based on feedback. This is what "agentic capabilities" typically means in practice.

---

### Level 3: Collaborative Multi-Agent System

Multiple specialized agents working together. One agent might handle data retrieval, another reasoning about implications, a third generating responses. A coordinator agent (or orchestration logic) routes problems to the right specialist and synthesizes their work.

**Capability**: Decompose complex problems into specialist domains and coordinate solutions

**Example**: A system where one agent researches customer needs, another proposes technical solutions, a third evaluates feasibility, and a coordinator synthesizes recommendations.

---

### Level 4: Self-Evolving System

An agent that can create new tools, new sub-agents, or refine its own processes based on experience. This is the frontier—systems that don't just execute predefined workflows but actively design and improve their own capabilities.

**Capability**: Autonomously create new tools or agents to handle new problems

**Example**: An agent that encounters a recurring problem, recognizes it needs a specialized capability, creates a tool or sub-agent to handle it, and integrates that new capability into its future workflows.

---

## Where Do You Fit Into This Taxonomy?

You've been working with **Level 2** systems. Claude Code demonstrates multi-step planning (analyze the problem, design a solution, implement in stages, test, refine). It manages context—deciding what information is relevant at each step. It iterates based on your feedback. These are Level 2 capabilities.

When you think about agent development, you're not starting from scratch. You already understand how LLMs reason, how to use tools (APIs, code execution), and how to think about specifications (from Part 4). The shift is understanding how to design systems that operate in this multi-step, context-aware, feedback-loop model—and eventually, how to orchestrate multiple agents (Level 3) or create self-improving systems (Level 4).

## The Paradigm Shift: Director vs Bricklayer

The emergence of agents represents a fundamental shift in how developers think about building systems. The paper articulates this shift using a powerful metaphor:

> "The traditional developer acts as a 'bricklayer,' precisely defining every logical step. The agent developer is more like a director—setting the scene, selecting the cast, providing context."

**Traditional Development (Bricklayer)**:
- You write code that controls *every* decision: if X, then Y; if Z, then A
- You specify the exact sequence of operations
- You handle every edge case explicitly
- The system does exactly what you programmed, nothing more

**Agent Development (Director)**:
- You specify the *goal* and provide context
- The agent reasons about how to achieve that goal
- You write specifications and provide examples of good outcomes
- The agent adapts to situations you didn't explicitly program for

**Practical Example**:

**Bricklayer approach** (traditional): Write code that authenticates a user, checks permissions, fetches data, transforms it, validates it, formats it, and returns it. Every step is explicit control flow.

**Director approach** (agent): Provide the agent with access to authentication tools, permission systems, data sources, and validation rules. Tell the agent: "A user has requested customer data. Verify they're authorized, fetch what they're allowed to see, and present it clearly." The agent reasons about the steps, adapts if permissions are denied, retries failed data fetches, and decides on the best presentation format.

This shift has profound implications:

**For Building**: You move from specifying *implementation* to specifying *intent*. Instead of "call function A, then B, then C," you're writing specifications that describe what success looks like and letting the agent figure out how.

**For Reliability**: You move from "did I handle every case?" to "did I provide enough context and feedback for the agent to handle cases well?" Agent systems use evaluation frameworks (testing against rubrics) and feedback loops to improve.

**For Complexity**: You can tackle problems that would require enormous amounts of control-flow code. A reservation system with an agent might adapt to cancellations, suggest alternatives, and handle disputes—without you programming every scenario.

---

## Career Implications: Why This Matters to You

The paradigm shift has real consequences for employment and career development.

**The transformation isn't replacement; it's transformation**. Jobs don't disappear; workflows change. A customer service agent might handle routine inquiries, but it needs human "directors" to:
- Design the agent (what it should do, what it shouldn't)
- Evaluate its performance (does it satisfy customers?)
- Handle escalations (when the agent encounters cases it shouldn't decide alone)
- Improve it iteratively (feedback loops, new capabilities)

**The skill premium is accelerating**. AI fluency is now the fastest-growing skill category. Within that, *agent design and orchestration* is emerging as the highest-value specialization. Companies building agent systems in 2025 will have severe talent shortages; developers who understand agent patterns will be in extraordinary demand.

**The mental models matter more than syntax**. You don't need to master every agent SDK (OpenAI, Google, Anthropic, LangChain). The frameworks change. But the mental models—how to think about agent goals, context management, evaluation, failure modes—transfer across all of them. This lesson teaches the mental models; Chapters 34-36 teach the SDKs.

---

## Try With AI

You now understand the 5-Level Taxonomy. Let's use it to classify real systems.

**Setup**: Open ChatGPT (chat.openai.com) or Claude (claude.ai). You'll classify several AI systems using the framework from this lesson.

**Classification Exercise 1: Claude Code**

Using the 5-Level Taxonomy, classify Claude Code.

**Prompt**:
```
I'm learning about AI agent classifications using this taxonomy:
- Level 0: LLM alone, no tools
- Level 1: LLM + tools for real-time data
- Level 2: Multi-step planning with context optimization
- Level 3: Multiple specialized agents coordinated
- Level 4: Self-evolving systems that create new tools

Claude Code is an AI development assistant that can:
1. Analyze codebases and understand requirements
2. Write code across multiple files
3. Run tests and observe results
4. Refactor based on feedback
5. Adapt its approach when tests fail

What level of the taxonomy does Claude Code fit, and why?
```

**Expected Outcome**: The AI should recognize Claude Code as **Level 2**. Here's why: It performs multi-step planning (analyze → design → implement → test → refine). It manages context—deciding what code to look at and what solutions are appropriate. It adapts based on feedback (test failures, your corrections). These are Level 2 capabilities.

---

**Classification Exercise 2: ChatGPT vs ChatGPT with Browsing**

Understand the difference between abstraction levels.

**Prompt**:
```
Compare these two scenarios using the 5-Level Taxonomy:

Scenario A: ChatGPT (standard) answering "What's the stock price of Apple?"
Scenario B: ChatGPT with web browsing enabled, answering the same question

How would you classify each scenario, and why does the ability to browse move it to a different level?
```

**Expected Outcome**: The AI should explain:
- **Scenario A** (no browsing) = Level 0 (generates response based on training data, which is outdated)
- **Scenario B** (with browsing) = Level 1 (can access real-time data via tools)

This illustrates how a single capability—tool access—shifts the level.

---

**Classification Exercise 3: Personal Experience**

Apply the taxonomy to a system you use.

**Prompt**:
```
Think about an AI system you use regularly (ChatGPT, Claude, GitHub Copilot, your phone's assistant, etc.).

Describe what it does, then classify it using the 5-Level Taxonomy. Be specific about which capabilities put it at that level.
```

**Expected Outcome**: You should be able to articulate why your chosen system is at its level based on concrete capabilities (tool access, planning, multi-agent coordination, etc.).

---

**Optional Stretch: The Director Paradigm**

Deepen your understanding of the paradigm shift.

**Prompt**:
```
A traditional developer (bricklayer) writes a function like this:

```javascript
function processOrder(order) {
  if (order.status === 'pending') {
    checkInventory(order.items);
    if (inventoryAvailable) {
      chargeCard(order.payment);
      if (cardSuccessful) {
        shipOrder(order);
        sendConfirmationEmail();
      } else {
        markOrderFailed();
      }
    } else {
      notifyOutOfStock();
    }
  }
}
```

An agent developer would approach the same problem differently. How would a director specify this workflow instead of writing the code above? What would they tell an agent to do?
```

**Expected Outcome**: The AI should articulate the director approach:
- Specify the goal: "Process this order"
- Provide context: "Here's the inventory system, payment processor, shipping system, and notification service"
- Provide rules: "Only charge if inventory is available. Only ship if payment succeeds. Always notify the customer."
- Let the agent reason: The agent decides the sequence, handles failures, adapts to edge cases

This shifts from *control flow* (explicit if-then-else) to *specification* (goal + context + rules).

---

**Safety Note**: As you use AI to explore these concepts, pay attention to how the AI reasons. Does it make assumptions? Does it ask clarifying questions? Notice how your feedback shapes its responses—that interaction illustrates the "director" role in action.
