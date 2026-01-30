"""
Project: edu_assistant
Component: orchestrator service (LLM core)
Responsibility:
  Interpret user intent and return structured interpretation artifacts.

Architectural Notes:
  - Centralizes reasoning and planning; does not execute actions directly.
  - Delegates execution to tools/connectors and relies on policy gates.

Related Documentation:
  - docs/*/architecture.md
  - docs/*/vision.md
  - AGENTS.md

Important Constraints:
  - No direct side effects or external system calls here.
  - Preserve separation between intention, orchestration, and execution.
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="edu_assistant - orchestrator", version="0.1.0")


class InterpretIn(BaseModel):
    text: str


@app.get("/health")
def health():
    # Liveness probe only; no orchestration logic should live here.
    return {"ok": True}


@app.post("/v1/interpret")
def interpret(payload: InterpretIn):
    # Public orchestration boundary: interpret input, do not execute actions.
    text = payload.text.strip()

    # MVP response (no LLM yet). Future: planner + tool selection + trace.
    # This must remain side-effect free; execution belongs to tools/connectors.
    return {
        "intent": {
            "type": "user_message",
            "confidence": 0.5,
        },
        "input_text": text,
        "response_text": f"Received: {text}",
        "trace": [
            {"step": "interpret", "detail": "MVP echo (replace with LLM planner)"},
        ],
    }
