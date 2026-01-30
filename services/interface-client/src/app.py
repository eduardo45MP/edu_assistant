#arquivo ./services/interface-client/src/app.py
"""
Project: edu_assistant
Component: interface-client service
Responsibility:
  Capture user input (text/audio), normalize it, and delegate to core services.

Architectural Notes:
  - Interface layer does not execute actions or interpret intent.
  - Delegates transcription to speech services and intent to orchestrator.

Related Documentation:
  - docs/*/architecture.md
  - docs/*/vision.md
  - AGENTS.md

Important Constraints:
  - Keep decisions and execution out of this service.
  - All side effects must be delegated and auditable upstream.
"""

from __future__ import annotations

import os
from typing import Optional

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import httpx

STT_URL = os.getenv("STT_URL", "http://speech-stt:8001")
ORCH_URL = os.getenv("ORCHESTRATOR_URL", "http://orchestrator:8002")

app = FastAPI(title="edu_assistant - interface-client", version="0.1.0")


class TextInput(BaseModel):
    text: str


@app.get("/health")
def health():
    # Liveness probe only; no user-facing logic here.
    return {"ok": True}

@app.post("/v1/input/text")
async def input_text(payload: TextInput):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{ORCH_URL}/v1/interpret",
            json={"text": payload.text.strip()},
        )
        r.raise_for_status()

    return {
        "input": {"text": payload.text},
        "orchestrator": r.json(),
    }

@app.post("/v1/input/audio")
async def input_audio(audio: UploadFile = File(...)):
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{STT_URL}/v1/transcribe",
            files={
                "audio": (
                    audio.filename,
                    await audio.read(),
                    audio.content_type or "application/octet-stream",
                )
            },
        )
        r.raise_for_status()

        text = r.json().get("text")

        if not text:
            raise HTTPException(status_code=502, detail="STT returned empty transcript")

        r2 = await client.post(
            f"{ORCH_URL}/v1/interpret",
            json={"text": text},
        )
        r2.raise_for_status()

    return {
        "input": {"audio": audio.filename},
        "transcript": text,
        "orchestrator": r2.json(),
    }