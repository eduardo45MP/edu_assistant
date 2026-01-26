# Architecture

## Purpose of this document

This document describes the high-level architecture of **edu_assistant**, focusing on system organisation, core components, responsibility boundaries, and the principles that guide architectural decisions throughout the project.

Its goal is **not** to specify detailed implementations, internal algorithms, or operational infrastructure configurations, but to establish a clear and shared view of **how the system is structured** and **why certain architectural decisions are made**.

This document **does not describe**:

* implementation details of individual services or modules
* definitive choices of vendors, models, or external APIs
* source code, usage examples, or complete technical contracts
* low-level decisions that may change as the project evolves

Those aspects should be addressed in dedicated technical documents, specifications, or directly in the codebase.

Over time, this document must evolve in an **incremental and intentional** manner, reflecting:

* relevant changes to the overall architecture
* introduction or removal of services
* significant changes in architectural style
* system and requirement maturation

This architecture description serves as a **living reference**, and must be updated whenever structural decisions affect how the system is understood, maintained, or extended.

---

## Architectural overview

The **edu_assistant** acts as an intermediary layer between the human user and the digital ecosystem, with the primary function of **translating human intent into coordinated computational actions**.

The system does not replace the human nor operate autonomously by default. Its role is to augment the user’s ability to interact with complex systems, reduce operational friction, and organise task execution based on commands expressed in natural language.

The relationship between human, orchestration, and execution is explicitly separated into three layers:

* **Human**: defines goals, expresses intent, authorises sensitive actions, and retains final control over meaningful decisions.
* **Orchestration**: interprets human intent, structures an execution plan, and coordinates the required components.
* **Execution**: performs concrete actions via services, tools, and external integrations, always within explicit permission and security boundaries.

This separation ensures that reasoning and planning are not coupled to direct execution, enabling stronger control, auditability, and independent evolution of components.

High-level architectural principles include:

* **Human in control by default**: no meaningful action occurs without explicit authorisation when required.
* **Intent before execution**: the system prioritises understanding what should be done before taking action.
* **Clear separation of responsibilities**: orchestration, execution, and interfaces evolve independently.
* **Transparency and traceability**: the system must be able to explain what was done, why it was done, and by which component.
* **Incremental evolution**: the architecture must allow growth and refinement without disruptive structural refactoring.

---

## Architectural style

The **edu_assistant** adopts a **distributed client–server model**, based on **microservices**, from its inception.

The system is organised as a set of independent services, each responsible for a specific functional domain and communicating through well-defined interfaces. An orchestration service acts as a logical coordinator, without executing actions directly, delegating responsibilities to specialised services.

### Rationale

The adoption of microservices is driven by characteristics intrinsic to the problem that edu_assistant aims to solve:

* The system is **naturally distributed**, involving multiple external integrations, data sources, and execution types.
* Different domains (orchestration, execution, voice, memory, integrations) have **distinct lifecycles, costs, and requirements**.
* Service isolation reduces the impact of failures and facilitates the application of **fine-grained security and permission policies**.
* The architecture supports incremental evolution, allowing capabilities to be added, removed, or replaced without deep structural rework.
* Specialised services are better suited for the future introduction of agents with clearly defined responsibilities.

This approach avoids excessive concentration of responsibilities and keeps the system aligned with its long-term vision.

### Implications of this decision

Choosing microservices brings explicit architectural consequences, consciously accepted:

* Higher operational complexity compared to monolithic architectures.
* The need for clear contracts, versioning, and governance between services.
* Dependence on well-defined synchronous and asynchronous communication mechanisms.
* Increased focus on observability, traceability, and fault handling.
* Greater initial organisational effort, offset by future flexibility and scalability.

These implications are considered part of the necessary cost to sustain a distributed, secure, and evolvable system over time.

---

## Logical system view

The logical view of **edu_assistant** organises the system into components with clearly defined responsibilities, maintaining a clear separation between **interface**, **orchestration**, **execution**, **integrations**, **data/memory**, and **control**.

Below are the main components, their responsibilities, and the boundaries between them.

---

### Main components

1. **Client / Interface**
2. **Orchestrator (LLM Core)**
3. **Execution Services (Tools)**
4. **Integration Services (Connectors)**
5. **Context and Memory Service**
6. **Policy, Permissions, and Security Service**
7. **Observability and Audit**

---

### Responsibilities of each component

#### 1) Client / Interface

Responsible for capturing user intent and presenting results.

Responsibilities:

* explicit activation trigger
* text and/or voice input (when applicable)
* presentation of responses (text, audio, notifications)
* display of confirmations when required

---

#### 2) Orchestrator (LLM Core)

Responsible for interpreting intent and coordinating execution.

Responsibilities:

* intent understanding and disambiguation
* generation of execution plans (steps + tools)
* selection of appropriate tools and connectors
* production of structured commands for execution
* generation of explanations/traces for plans and results

---

#### 3) Execution Services (Tools)

Responsible for executing concrete actions with safety and predictability.

Responsibilities:

* execution of idempotent actions where possible
* input and output validation (schemas)
* application of execution limits (timeouts, retries, rate limits)
* return of standardised responses to the orchestrator
* logging and auditing of executed actions

Examples:

* calendar (create/update events)
* automation (repetitive tasks)
* messaging (drafts, assisted replies with approval)
* computation (calculations, transformations)

---

#### 4) Integration Services (Connectors)

Responsible for accessing external systems and normalising data.

Responsibilities:

* authentication and authorisation with external platforms
* data collection and normalisation
* enforcement of provider-specific limits and policies
* delivery of data to the system in a consistent format

Examples:

* email
* documents
* chats/messaging (when applicable)
* web search and public/private data sources

---

#### 5) Context and Memory Service

Responsible for storing and serving short- and long-term context.

Responsibilities:

* session context (short-term memory)
* opt-in persistent memory
* user preferences and configuration
* cleanup, expiration, and removal mechanisms
* support for retrieval mechanisms (e.g. RAG), when applicable

---

#### 6) Policy, Permissions, and Security Service

Responsible for controlling what can and cannot be executed.

Responsibilities:

* risk classification per action
* permission gates per tool and domain
* enforcement of human approval for sensitive actions
* application of privacy and security rules
* blocking and limitation mechanisms to prevent abuse

---

#### 7) Observability and Audit

Responsible for system traceability and transparency.

Responsibilities:

* structured and traceable logging
* audit trails for tool calls and results
* performance and quality metrics
* support for debugging and failure inspection
* generation of human-readable traces (when enabled)

---

### Clear boundaries between components

To maintain predictability and safety, the following boundaries are considered invariant:

* **The interface does not execute actions**: it only captures intent and presents results or authorisations.
* **The orchestrator does not execute actions directly**: it only interprets, plans, and coordinates.
* **Tools execute actions**: but do not decide goals or invent intent.
* **Connectors access external data**: but do not perform irreversible actions without passing through policy checks.
* **Memory is not implicit**: persistence requires explicit control and consent.
* **Permissions are transversal and mandatory**: no sensitive action bypasses the policy layer.
* **Audit is part of the system**: it is not optional when execution or sensitive data access occurs.

These boundaries ensure the system evolves in a safe, modular, and auditable manner, even as complexity increases over the roadmap.

---

## Service organisation

The **edu_assistant** architecture is organised as a set of independent services, each responsible for a specific functional domain. This organisation reinforces the separation between **intent**, **orchestration**, **execution**, **integration**, **persistence**, and **control**, enabling domain-level evolution and scalability.

---

### Interface / client service

Responsible for all direct interaction with the user.

Main functions:

* capture user commands and intents (text or voice)
* manage explicit activation triggers
* present responses, confirmations, and notifications
* forward requests to the orchestration service

Characteristics:

* does not execute actions or access external systems
* may exist in multiple forms (CLI, local app, wearable, web)
* maintains minimal state, focused on user experience

---

### Orchestration service (LLM core)

Responsible for interpreting human intent and coordinating the system.

Main functions:

* interpret and disambiguate natural language commands
* generate structured action plans
* select appropriate execution and integration services
* request permission validation when required
* consolidate results and produce explainable responses

Characteristics:

* does not execute actions directly
* does not access external systems without mediation
* acts as the system’s logical coordinator
* centralises reasoning, not side effects

---

### Execution services (tools)

Responsible for executing concrete, controlled actions.

Main functions:

* execute specific operations (e.g. create events, send messages, run automations)
* validate input and output schemas
* apply execution limits (timeouts, retries, rate limits)
* record actions for auditing

Characteristics:

* each service is specialised in a specific action domain
* executes only what was explicitly requested
* does not interpret intent or decide objectives
* designed to be idempotent whenever possible

---

### Integration services (connectors)

Responsible for communication with external systems and platforms.

Main functions:

* authenticate and authorise access to external services
* collect, transform, and normalise data
* apply provider-specific policies and limits
* provide data to other services in a consistent manner

Characteristics:

* isolate external dependencies
* do not perform irreversible actions without passing through policy checks
* facilitate replacement or removal of integrations
* reduce the impact of external API changes

---

### Memory services

Responsible for storing and providing context over time.

Main functions:

* maintain session memory (short-term)
* store persistent memory with explicit user consent
* manage user preferences and configuration
* provide query, cleanup, and removal mechanisms

Characteristics:

* no data is stored without authorisation
* memory is always auditable and user-controllable
* designed to evolve incrementally (short → long term)

---

### Transversal services (policies, security, audit)

Responsible for ensuring safe and controlled system operation.

Main functions:

* evaluate risk and permissions per action or service
* require human approval for sensitive actions
* apply privacy and usage rules
* maintain complete audit trails
* provide system visibility and traceability

Characteristics:

* mandatory services, not optional
* applied consistently across all flows
* independent from business logic
* fundamental for system trust and scalability

---

This service organisation establishes clear boundaries and reinforces the core idea of edu_assistant: **orchestrating human intent with safe, controlled, and auditable execution**, without improper coupling between responsibilities.

---

## Inter-service communication

Communication between **edu_assistant** services is based on explicit contracts and well-defined patterns, ensuring predictability, fault isolation, and independent evolution of components.

The system combines **synchronous** and **asynchronous** communication, selected according to interaction type, expected latency, and operational impact.

---

### Synchronous communication patterns

Synchronous communication is used when immediate responses or direct user interaction are required.

Typical cases:

* interface → orchestrator
* orchestrator → policy/permission services
* orchestrator → data query services
* context retrieval for planning

Characteristics:

* based on HTTP/REST APIs
* structured payloads validated by schema
* explicit and short timeouts
* deterministic responses with no hidden side effects

Rule:

> Synchronous communication **must not** trigger irreversible actions without passing through permission validation.

---

### Asynchronous communication patterns

Asynchronous communication is used for action execution, automations, and tasks that may occur outside the immediate interaction flow.

Typical cases:

* tool execution
* automations and workflows
* long-running tasks
* external data collection and processing

Characteristics:

* based on queues or events
* decoupling between orchestration and execution
* support for retries and backoff
* tolerance to latency and temporary failures

Rule:

> Every asynchronous execution must be traceable and correlated to an explicit intent and authorisation.

---

### Contracts and versioning

Inter-service communication is governed by explicit contracts.

Guidelines:

* each service exposes clear input and output contracts
* schemas are explicitly versioned
* incompatible changes require a new contract version
* versioning is preferably semantic

Best practices:

* avoid implicit behavioural dependencies
* document contracts alongside code
* maintain backward compatibility whenever possible

---

### Failure handling

Failures are treated as an expected part of a distributed system.

Adopted principles:

* failures must be isolated and not cascade
* timeouts and circuit breakers must be explicit
* retries must be controlled and idempotent
* failures must be visible and auditable

Expected behaviour:

* external service errors must not compromise the orchestration core
* the system should return understandable responses to the user when appropriate
* intermediate states must remain consistent and recoverable

Failure handling is considered an integral part of the architecture and essential to maintaining reliability and predictability as the system evolves.

---

## Execution model

The execution model of **edu_assistant** describes how a request flows through the system, from the user’s expression of intent to action execution and the delivery of results. This model emphasises **explicit control**, **conscious decision-making**, and **transparency**.

---

### Typical request flow

A request generally follows these steps:

1. **Activation**
   The user explicitly activates the system through the interface (command, touch, keyword).

2. **Intent capture**
   The interface collects user input in text or voice form.

3. **Pre-processing**
   If the input is voice-based, it is transcribed into text before being sent to the orchestrator.

4. **Interpretation**
   The orchestration service analyses the input, interprets the intent, and identifies possible actions.

5. **Planning**
   The orchestrator generates a structured plan containing the required steps, involved services, and parameters.

6. **Policy validation**
   The plan is evaluated by the policy and permissions service to identify risks and authorisation requirements.

7. **Human authorisation**
   When required, the user is asked to confirm or deny sensitive actions.

8. **Execution**
   After validation and authorisation, the plan is executed by the appropriate services, either synchronously or asynchronously.

9. **Result aggregation**
   The results of the executions are collected and normalised.

10. **User response**
    The system presents the final result through the interface.

11. **Context registration**
    Relevant context is stored as session memory or persistent memory, when authorised.

---

### Decision points

During the execution flow, the system makes explicit decisions such as:

* intent interpretation and disambiguation
* selection among multiple possible plans
* definition of which tools and services will be used
* choice between synchronous and asynchronous execution
* assessment of risk associated with proposed actions

These decisions are centralised in the orchestration service and validated by control layers when necessary.

---

### Human authorisation points

The system requires explicit human authorisation in situations such as:

* execution of irreversible actions
* sending messages or external communications
* publishing content on external platforms
* accessing or modifying sensitive data
* recurring or long-running automations

Authorisation must be clear, contextual, and understandable, allowing the user to understand **what will be done and why**.

---

### Results and traces

The response returned to the user includes:

* the primary result of the request
* confirmation or error messages, when applicable
* concise explanations of executed actions (trace)

When enabled, traces must:

* describe executed steps in understandable language
* indicate which services were invoked
* record relevant decisions made by the system

This mechanism ensures transparency, facilitates auditing, and strengthens user trust in the operation of the system.

---

## Data, context, and memory

The **edu_assistant** handles data across different durations and sensitivity levels. The architecture treats **data**, **context**, and **memory** as distinct concepts, with clear rules for usage, persistence, and control, avoiding implicit or opaque accumulation of user information.

---

### Types of data handled

The system primarily deals with the following data types:

* **Input data**: text or voice commands provided by the user.
* **Context data**: temporary information required to interpret and continue an interaction.
* **Operational data**: parameters, results, and intermediate states produced during tool execution.
* **Integration data**: information obtained from authorised external systems.
* **Memory data**: information stored to improve future interactions.
* **Audit data**: technical records of actions, decisions, and accesses.

Each data type has specific rules governing retention, visibility, and access.

---

### Short-term context

Short-term context represents the temporary state of an interaction or session.

Characteristics:

* limited to the duration of a specific session or flow
* used to maintain continuity between related commands
* automatically discarded at the end of the session, unless explicitly authorised

Examples:

* references to recently executed actions
* resolution of pronouns and implicit commands (“this”, “that”)
* continuation of a previously started task

Short-term context is not considered persistent memory.

---

### Long-term persistence

Long-term persistence is optional and depends on explicit user consent.

Characteristics:

* stores information relevant to personalisation or future efficiency
* may include preferences, recurring patterns, or approved data
* always associated with a clearly defined purpose

Constraints:

* no data is persisted without authorisation
* persisted data must be editable and removable
* the system must be able to explain why a given piece of data was stored

---

### User control and transparency

The user retains full control over their data and memory.

Adopted principles:

* visibility into what is being stored
* ability to review, edit, or delete persisted data
* clear distinction between temporary context and long-term memory
* understandable explanations of how data is used in system decisions

Transparency in data usage is considered fundamental to trust and to the responsible evolution of edu_assistant.

---

## Security, permissions, and control

Security in **edu_assistant** is treated as a structural element of the architecture, not as an auxiliary layer. The system is designed to operate with **explicit control**, **least privilege**, and **full traceability**, preserving user autonomy and reducing operational risk.

---

### Permission model

The permission model is based on **explicit authorisations per action and per domain**.

Characteristics:

* permissions are granted by action type, not generically
* services and tools operate with least privilege
* permissions may be temporary, revocable, or conditional
* no action assumes implicit authorisation

The system evaluates permissions at runtime, taking context, risk, and declared intent into account.

---

### Sensitive actions

Sensitive actions are those that may produce irreversible effects, data exposure, or significant external impact.

Examples:

* sending messages or external communications
* publishing content on external platforms
* permanent modification of user data
* recurring or long-running automations
* access to personal or confidential information

These actions require additional validation and, in general, explicit user confirmation before execution.

---

### Human in control

**Human in control** is a core principle of the system.

Guidelines:

* the system never executes sensitive actions without human authorisation
* the user can interrupt, cancel, or deny executions in progress
* critical decisions are always communicated clearly
* system autonomy is limited and contextual

Even when automations are permitted, they operate within previously defined and revocable boundaries.

---

### Audit and traceability

All relevant system actions are auditable.

Characteristics:

* structured logging of intents, decisions, and executions
* clear association between intent, authorisation, and executed action
* audit trails accessible for inspection
* traceability across services involved in a request

Auditability ensures transparency, facilitates failure diagnosis, and reinforces user trust in the operation of edu_assistant.

---

## Technology stack

The technology stack of **edu_assistant** is defined with a focus on **interoperability**, **incremental evolution**, and **fitness for a distributed system**, avoiding overly rigid dependencies. The choices described below represent an initial direction and may evolve as the project matures.

---

### Languages

* **Python**
  The primary language of the system, chosen for the maturity of its ecosystem in AI, automation, API integration, and rapid service development.

* **Other languages (when necessary)**
  Specific services may be implemented in other languages if performance, latency, or integration requirements justify it, provided that defined contracts are respected.

---

### Frameworks

* **APIs and services**
  Lightweight web frameworks for building HTTP APIs, with support for schema validation, versioning, and documentation.

* **Orchestration and AI**
  Libraries and SDKs for integrating language models, context retrieval mechanisms, and tool coordination.

* **Messaging and asynchronous execution**
  Tools for queues, events, and asynchronous processing, suitable for distributed systems.

Specific framework choices should prioritise simplicity, clarity, and broad adoption.

---

### Protocols

* **HTTP/REST**
  The primary protocol for synchronous communication between services.

* **Queue- or event-based messaging**
  Used for asynchronous execution, automations, and long-running tasks.

* **Authentication and authorisation protocols**
  Employed for access control between services and external integrations.

Inter-service communication must always be explicit, authenticated, and versioned.

---

### Infrastructure (conceptual level)

Infrastructure is designed to support a distributed system in a gradual manner.

Adopted concepts:

* independently running services
* isolation of critical components
* ability to scale by functional domain
* use of containers for execution standardisation
* separation of development, testing, and production environments

Infrastructure orchestration and the level of automation should evolve as system complexity and usage increase.

---

## Evolution strategy

The evolution strategy of **edu_assistant** prioritises continuous and controlled growth, avoiding architectural disruptions and ensuring that the system remains usable and understandable over time.

---

### Incremental growth

The system should evolve in small steps, always delivering functional value before introducing additional layers of complexity.

Guidelines:

* new capabilities are introduced as isolated services or extensions
* experimental features do not compromise the existing core
* each evolution step must be independently verifiable
* the system must remain usable at all stages of maturity

This model enables continuous learning and course correction without the need for deep structural rework.

---

### Change isolation

Changes should be isolated as much as possible to reduce impact and risk.

Principles:

* services have clearly defined responsibilities
* changes in one service should not require changes in others
* external dependencies are encapsulated by connectors
* explicit contracts reduce implicit coupling

Isolation facilitates maintenance, testing, and component replacement over time.

---

### Version compatibility

Compatibility is treated as an architectural requirement.

Adopted practices:

* explicit versioning of APIs and contracts
* maintenance of backward compatibility whenever possible
* introduction of new versions without immediate breaking of existing ones
* planned and documented deprecation of older versions

These practices ensure that the system can evolve without disrupting existing flows or creating fragile dependencies.

---

## Out of architectural scope

This document explicitly defines boundaries to avoid premature decisions or incorrect expectations regarding the scope of **edu_assistant**.

### Explicitly excluded decisions

The following decisions are **not** part of the current architectural scope:

* definition of a final commercial product or business model
* guarantees of full system autonomy
* implementation of implants, prosthetics, or invasive interfaces
* guarantees of clinical, medical, or legal use
* extreme performance optimisations at the expense of clarity and safety
* mandatory dependency on a specific AI or infrastructure vendor

These decisions may be revisited in the future, but they do not guide the architecture at this stage.

---

### Conscious system boundaries

edu_assistant acknowledges deliberate architectural limits:

* the system acts as an **orchestrator**, not as an unrestricted autonomous agent
* critical decisions remain under human control
* data persistence is limited and opt-in
* the system prioritises predictability and auditability over “magic”
* the architecture avoids tight coupling that would hinder evolution or inspection

These boundaries are considered fundamental to keeping the project sustainable and responsible.

---

## Architectural principles

The following principles guide present and future decisions in **edu_assistant**.

### Decision-guiding principles

* **Human in control by default**
* **Intent before execution**
* **Clear separation of responsibilities**
* **Explicit contracts between services**
* **Transparency and traceability**
* **Conscious incremental evolution**

---

### Accepted trade-offs

The project consciously accepts the following trade-offs:

* higher operational complexity in exchange for modularity and isolation
* slower initial development speed in favour of future scalability
* additional observability and security costs to ensure trust
* explicit and verifiable decision paths instead of opaque automation

These trade-offs reflect the priority given to building a reliable and evolvable system.

---

### Criteria for future changes

Architectural changes should be evaluated based on:

* impact on user safety and control
* preservation of the separation between intent, orchestration, and execution
* compatibility with existing contracts
* clarity and auditability of the resulting system
* concrete benefits relative to the complexity introduced

Any significant change must be documented and reflected in this document, keeping the architecture as a living reference for the project.

---

## Suggested project tree

```
edu_assistant/
├─ README.md
├─ README.pt.md
├─ AGENTS.md
├─ LICENSE
├─ .gitignore
├─ .env.example
├─ docker-compose.yml
├─ docs/
│  ├─ en-GB/
│  │  ├─ README.md
│  │  ├─ vision.md
│  │  ├─ architecture.md
│  │  ├─ setup.md
│  │  ├─ use-cases.md
│  │  └─ roadmap.md
│  └─ pt-BR/
│     ├─ README.md
│     ├─ visao.md
│     ├─ arquitetura.md
│     ├─ setup.md
│     ├─ casos-de-uso.md
│     └─ roadmap.md
│
├─ shared/
│  ├─ contracts/
│  │  ├─ openapi/
│  │  ├─ schemas/
│  │  └─ versions.md
│  ├─ libs/
│  │  ├─ logging/
│  │  ├─ tracing/
│  │  ├─ auth/
│  │  ├─ errors/
│  │  └─ utils/
│  └─ README.md
│
├─ services/
│  ├─ interface-client/
│  ├─ orchestrator/
│  ├─ policy-permissions/
│  ├─ memory/
│  ├─ audit-observability/
│  ├─ tools/
│  ├─ connectors/
│  └─ speech/
│
├─ infra/
│  ├─ docker/
│  ├─ k8s/
│  ├─ observability/
│  └─ README.md
│
├─ scripts/
│  ├─ dev_up.sh
│  ├─ dev_down.sh
│  ├─ lint.sh
│  ├─ test.sh
│  └─ format.sh
│
└─ tests/
   ├─ integration/
   └─ e2e/
```