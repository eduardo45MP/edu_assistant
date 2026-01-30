"""
Project: edu_assistant
Component: speech-stt service
Responsibility:
  Convert audio input into text for downstream interpretation.

Architectural Notes:
  - Provides transcription only; it does not interpret intent or execute actions.
  - Acts as a supporting execution service for the interface layer.

Related Documentation:
  - docs/*/architecture.md
  - docs/*/vision.md
  - AGENTS.md

Important Constraints:
  - Keep transcription deterministic and auditable.
  - No side effects beyond returning text.
"""

from __future__ import annotations

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI(title="edu_assistant - speech-stt", version="0.1.0")


@app.get("/health")
def health():
    # Liveness probe only; no processing logic here.
    return {"ok": True}


@app.post("/v1/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    """
    MVP stub:
    - Receives audio and returns a placeholder transcript.
    - Replace this with Whisper/local/provider later.
    """
    # Transcription boundary: this service never interprets intent or triggers actions.
    _ = await audio.read()  # consume stream (avoid unused warning)
    return JSONResponse({"text": "[stub transcript] replace STT implementation"})
