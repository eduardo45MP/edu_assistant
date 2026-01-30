from __future__ import annotations

import os
from typing import Optional

import httpx
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel


STT_URL = os.getenv("STT_URL", "http://speech-stt:8001")
ORCH_URL = os.getenv("ORCHESTRATOR_URL", "http://orchestrator:8002")

app = FastAPI(title="edu_assistant - interface-client", version="0.1.0")


class TextInput(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/v1/input")
async def input_endpoint(payload: Optional[TextInput] = None, audio: UploadFile | None = File(default=None)):
    """
    Accepts either:
      - JSON body: {"text": "..."}
      - multipart/form-data: audio=@file.wav (or mp3/m4a)
    """
    transcript: Optional[str] = None

    async with httpx.AsyncClient(timeout=30) as client:
        if audio is not None:
            # Transcribe audio
            files = {"audio": (audio.filename, await audio.read(), audio.content_type or "application/octet-stream")}
            try:
                r = await client.post(f"{STT_URL}/v1/transcribe", files=files)
                r.raise_for_status()
            except Exception as e:
                raise HTTPException(status_code=502, detail=f"STT failed: {e}")

            transcript = r.json().get("text")
            if not transcript:
                raise HTTPException(status_code=502, detail="STT returned empty transcript")

            text = transcript
        else:
            if payload is None or not payload.text.strip():
                raise HTTPException(status_code=400, detail="Provide JSON {'text': '...'} or multipart audio")
            text = payload.text.strip()

        # Send to orchestrator
        try:
            r2 = await client.post(f"{ORCH_URL}/v1/interpret", json={"text": text})
            r2.raise_for_status()
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Orchestrator failed: {e}")

        return {
            "input": {"text": payload.text if payload else None, "audio": audio.filename if audio else None},
            "transcript": transcript,
            "orchestrator": r2.json(),
        }