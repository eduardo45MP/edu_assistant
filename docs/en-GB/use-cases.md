# Use Cases - edu_assistant

This document describes the **main use cases explored** by the **edu_assistant** project.  
The scenarios presented here do not represent guaranteed final features, but rather **application directions** that guide architectural, technical, and ethical decisions.

All use cases respect the project’s core principles:

- human in control by default  
- explicit intention before execution  
- separation between decision, orchestration, and action  
- transparency and auditability  

---

## 1. Calendar and schedule management

### Description
The assistant helps the user create, modify, and query calendar events using natural language commands.

### Examples
- “Schedule a meeting tomorrow at 2pm with the team.”
- “Reschedule that meeting to Friday morning.”
- “What do I have this afternoon?”

### Typical flow
1. The user expresses an intention  
2. The orchestrator interprets and disambiguates date/time  
3. Permission validation  
4. Execution via the calendar tool  
5. Clear confirmation to the user  

### Notes
- Creating or modifying events requires explicit authorisation  
- The system does not assume sensitive context without confirmation  

---

## 2. Interaction continuity and context

### Description
The system maintains **short-term context** to enable natural, continuous interactions without constant repetition.

### Examples
- “Reschedule that meeting.”
- “Continue the research we started earlier.”
- “Summarise that.”

### Limits
- Context is temporary  
- There is no automatic long-term memory persistence  
- Ambiguities trigger clarification requests  

---

## 3. Assisted technical and scientific research

### Description
The assistant supports research across authorised technical, scientific, or documentary sources, acting as a **curator and synthesiser**, not as a primary source.

### Examples
- “Research recent articles on LLM orchestration.”
- “Summarise the main points of this paper.”
- “Compare these two approaches.”

### Capabilities
- multi-source search  
- structured synthesis  
- conceptual comparison  
- source attribution  

---

## 4. Search and correlation across authorised communications

### Description
edu_assistant can assist in searching and organising information from emails, messages, or documents, **only with explicit authorisation**.

### Examples
- “Find important emails from today.”
- “Is there any message from João about the contract?”
- “Summarise the recurring topics in this conversation.”

### Restrictions
- access limited to authorised sources  
- no automatic replies without approval  
- mandatory logging and audit trails  

---

## 5. Assisted writing (with human approval)

### Description
The assistant helps with **drafting text**, but never sends external communications without human validation.

### Examples
- “Draft a polite reply to this email.”
- “Write a professional message confirming the meeting.”

### Flow
1. Draft generation  
2. Presentation to the user  
3. Manual adjustments (if desired)  
4. Explicit approval before any sending  

---

## 6. Automation of repetitive tasks

### Description
The system can execute **limited, explicit, and revocable automations**, always within clearly defined scopes.

### Examples
- “Every Friday, summarise my meetings for the week.”
- “Notify me when an email with this subject arrives.”

### Limits
- automations require explicit consent  
- clearly defined scope  
- cancellation possible at any time  

---

## 7. Contextual recommendations

### Description
edu_assistant can suggest options based on user-provided context, without assuming implicit preferences.

### Examples
- “Suggest nearby restaurants.”
- “Give me tool options for this problem.”

### Principle
Recommendation ≠ decision.  
The final choice always belongs to the user.

---

## 8. Wearable device integration (exploratory)

### Description
Exploration of discreet interactions through wearable devices, such as bone-conduction headphones.

### Examples
- contextual alerts  
- brief reminders  
- short audio responses  

### Note
This use case is **experimental** and depends on further technical and ethical validation.

---

## 9. Intelligent alerts and notifications

### Description
The assistant can emit alerts based on predefined events, rules, or context.

### Examples
- “Notify me if this meeting is delayed.”
- “Alert me if this document changes.”

### Limits
- alerts are opt-in  
- no implicit surveillance  
- clear and transparent rules  

---

## Explicitly out of scope

edu_assistant does **not** aim to:

- act as an unrestricted autonomous agent  
- make strategic decisions on behalf of the user  
- execute sensitive actions without authorisation  
- operate as a clinical, medical, or legal system  
- store personal data without consent  

---

## Final note

The use cases presented here serve as a **guide to intent**, not as product promises.

The goal of edu_assistant is not to maximise automation,  
but to **reduce friction between human intention and computational action**,  
while preserving control, clarity, and responsibility.

This document should evolve alongside the project.