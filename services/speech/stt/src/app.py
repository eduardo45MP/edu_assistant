from __future__ import annotations

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI(title="edu_assistant - speech-stt", version="0.1.0")


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/v1/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    """
    MVP stub:
    - Receives audio and returns a placeholder transcript.
    - Replace this with Whisper/local/provider later.
    """
    _ = await audio.read()  # consume stream (avoid unused warning)
    return JSONResponse({"text": "[stub transcript] replace STT implementation"})