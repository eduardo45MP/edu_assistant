from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="edu_assistant - orchestrator", version="0.1.0")


class InterpretIn(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/v1/interpret")
def interpret(payload: InterpretIn):
    text = payload.text.strip()

    # MVP response (no LLM yet)
    # Later: planner + tool_selection + trace
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