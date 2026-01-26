# AGENTS

## Purpose

This project adopts an **agent-oriented architecture**.

Agents are logical entities responsible for executing well-defined tasks, operating within explicit boundaries, and collaborating with humans and other agents to evolve the system in a predictable, auditable, and scalable way.

Agents exist to **amplify human capability**, not to replace human judgement.

---

## What is an Agent

An **Agent** is an autonomous or semi-autonomous unit that:

- Has a **clear and limited purpose**
- Operates within **explicit rules and constraints**
- Executes specialised or repeatable tasks
- Produces **verifiable and traceable outputs**
- Interacts with code, documentation, tools, APIs, or humans
- Can be coordinated by a central orchestrator

Agents are not simple scripts.  
They represent **intelligent operational roles** within the system.

---

## Core Principles

All agents in this repository must comply with the following principles:

### 1. Clear Scope
An agent must do **one thing well**.

Anything outside its declared scope is explicitly forbidden.

---

### 2. Controlled Autonomy
Agents may act independently **only within predefined limits**.

Autonomy is a tool - not a default right.

---

### 3. Human-in-the-Loop
Final responsibility **always remains with humans**.

Agents must:
- request approval for sensitive actions
- expose their reasoning when relevant
- defer decisions when uncertainty exceeds defined thresholds

---

### 4. Auditability
Every meaningful action performed by an agent must be:
- traceable
- explainable
- attributable

No silent side effects. No opaque decisions.

---

### 5. Separation of Responsibilities
Agents do **not**:
- redefine system goals
- expand their own scope
- modify unrelated domains
- bypass policy or permission layers

Each agent evolves independently, without breaking others.

---

## Types of Agents (Examples)

This project may include - but is not limited to - the following agent types:

### Code Agents
- Generate, refactor, or review code
- Respect architectural contracts
- Never introduce hidden behaviour

### Documentation Agents
- Create and maintain documentation
- Ensure consistency across languages
- Reflect architectural reality, not aspirations

### QA / Review Agents
- Validate quality, consistency, and standards
- Detect regressions or conceptual drift

### Planning Agents
- Assist with roadmap structuring
- Decompose goals into actionable steps
- Provide options, not decisions

### Tool or Domain Agents
- Specialised agents tied to a specific domain (calendar, messaging, research, computation)
- Execute actions only via approved tools

---

## Agent Documentation Requirements

Every agent introduced into the project **must** be documented with:

- **Name**
- **Purpose**
- **Responsibilities**
- **Explicit non-responsibilities** (what it does *not* do)
- **Inputs**
- **Outputs**
- **Dependencies** (human or technical)
- **Permission level**
- **Failure modes**

Undocumented agents are considered invalid.

---

## Boundaries and Restrictions

Agents must **never**:

- Make irreversible strategic decisions without human validation
- Persist memory or data without explicit authorisation
- Modify policies, permissions, or security rules
- Act outside their declared scope
- Represent themselves as human decision-makers

Violating these boundaries is considered a design failure.

---

## Orchestration Model

Agents are coordinated by a **central orchestrator**.

- Agents do not self-assign goals
- Agents do not directly invoke other agents unless explicitly allowed
- The orchestrator manages:
  - sequencing
  - permissions
  - context
  - traceability

Agents execute.  
Humans decide.  
The orchestrator coordinates.

---

## Evolution Strategy

Agents are expected to evolve over time.

Guidelines for evolution:

- Extend capability without expanding scope
- Prefer composition over complexity
- Deprecate responsibly
- Update documentation with every meaningful change

This file is a **living document** and must evolve alongside the system.

---

## Final Statement

Agents are leverage.  
They reduce friction, increase consistency, and extend reach.

But direction, intent, and accountability  
**always belong to humans**.