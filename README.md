# edu_assistant

**edu_assistant** is a conceptual and experimental project that explores the creation of an **intention-driven intelligent assistant**, designed to act as a continuous cognitive and operational support layer between humans and computational systems.

More than a chatbot, edu_assistant investigates the idea of **human–machine functional symbiosis**, where natural language becomes the primary mechanism for orchestrating actions, systems, and decisions.

---

## Vision

The most significant recent breakthrough in computing was not only the evolution of AI models, but the practical feasibility of **bidirectional translation between human language and computational execution**.

edu_assistant is built on the following premise:

> Humans no longer need to speak the language of machines.  
> Machines are now capable of interpreting, structuring, and executing human intentions.

This project explores this shift as the foundation for a new class of systems:  
**intention-oriented assistants with explicit human control and auditable execution**.

---

## What is edu_assistant

edu_assistant is conceived as a **cognitive orchestrator**, capable of:

- interpreting natural language commands
- understanding intent and context
- planning actions in a structured manner
- coordinating tools, APIs, and external services
- executing actions with security, limits, and explicit authorisation

It is **not**:
- a traditional chatbot
- an unrestricted autonomous system
- an AI that replaces human decision-making

It is a **mediator between human intention and computational action**.

---

## Assis - the assistant identity

Within the project, the assistant adopts a distinct identity: **Assis**.

The name references both *assistant* and a human surname, reinforcing:
- proximity
- continuity
- personalisation
- natural interaction

Assis is activated **explicitly** and always operates within clearly defined permission and control boundaries.

---

## Core principles

The project is guided by clear principles:

- **Human in control by default**  
  No sensitive action occurs without explicit authorisation.

- **Intention before execution**  
  Understanding what should be done matters more than acting quickly.

- **Clear separation of responsibilities**  
  Orchestration, execution, integration, and interfaces evolve independently.

- **Transparency and traceability**  
  The system must be able to explain what was done, why, and by which component.

- **Incremental evolution**  
  The system grows in layers, avoiding disruptive refactors.

---

## Architectural vision (high level)

edu_assistant adopts a **distributed microservices-based architecture**, organised into clearly defined layers:

- **Interface / Client**  
  Captures commands (voice or text) and presents responses.

- **Orchestrator (LLM Core)**  
  Interprets intent, generates plans, and coordinates actions.

- **Execution Services (Tools)**  
  Perform concrete actions in a safe and predictable manner.

- **Integration Services (Connectors)**  
  Connect to external systems and normalise data.

- **Context and Memory**  
  Manage short-term context and opt-in persistent memory.

- **Policies, Permissions, and Security**  
  Control risk, authorisations, and execution boundaries.

- **Audit and Observability**  
  Ensure traceability, logging, and transparency.

> The orchestrator **never executes actions directly**.  
> Decision-making and execution are always separated.

---

## Repository structure (summary)

```text
edu_assistant/
├─ README.md
├─ README.pt-BR.md
├─ AGENTS.md
├─ docs/
│  ├─ en-GB/
│  └─ pt-BR/
├─ shared/
├─ services/
│  ├─ orchestrator/
│  ├─ interface-client/
│  ├─ memory/
│  ├─ policy-permissions/
│  ├─ audit-observability/
│  ├─ tools/
│  └─ connectors/
├─ infra/
├─ scripts/
└─ tests/
````

Detailed documentation for vision, architecture, setup, and roadmap is available in the `docs/` directory.

---

## Explored use cases

The project investigates, among others:

* calendar and schedule management
* search and correlation across authorised emails and messages
* technical and scientific research
* automation of repetitive tasks
* assisted writing with human approval
* contextual recommendations
* wearable device integration
* intelligent alerts and notifications

All actions are subject to **explicit user permission**.

---

## Roadmap (high-level)

* **Phase 1:** functional core and explicit commands
* **Phase 2:** context and interaction continuity
* **Phase 3:** tool expansion and automation
* **Phase 4:** multimodal interaction and wearables
* **Phase 5:** coordinated specialised agents
* **Phase 6:** long-term exploration (opt-in)

The complete roadmap is documented in `docs/en-GB/roadmap.md`.

---

## Project status

🚧 **Actively evolving project**
edu_assistant is experimental, iterative, and conceptually ambitious.
The current focus is on **validating architecture, interaction patterns, and safe boundaries** before advancing toward deeper automation.

---

## Licence

This project is distributed under the licence specified in the `LICENSE` file.

---

## Author

Created and maintained by **Eduardo Peixoto**
CEO at **Innoforge.tech**

> The goal is not to build an AI that replaces humans,
> but a system that **amplifies their ability to decide, act, and understand**
> in an increasingly complex digital world.