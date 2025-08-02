import asyncio
import tempfile
import os
from edge_tts import Communicate
import platform
import subprocess

async def _speak_async(text, voice="en-US-AriaNeural"):
    communicate = Communicate(text, voice)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmpfile:
        await communicate.save(tmpfile.name)
        audio_path = tmpfile.name

    # Play audio file depending on OS
    if platform.system() == "Windows":
        # Use Powershell to play mp3
        subprocess.run(["powershell", "-c", f"(New-Object Media.SoundPlayer '{audio_path}').PlaySync();"])
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["afplay", audio_path])
    else:
        # Linux - try mpg123 or mpv
        if subprocess.call(["which", "mpg123"], stdout=subprocess.DEVNULL) == 0:
            subprocess.run(["mpg123", audio_path])
        elif subprocess.call(["which", "mpv"], stdout=subprocess.DEVNULL) == 0:
            subprocess.run(["mpv", "--no-video", audio_path])
        else:
            print("⚠️ No suitable audio player found. Please install mpg123 or mpv.")

    os.remove(audio_path)

def speak(text, config):
    voice = config.get("voice_name", "en-US-AriaNeural")
    asyncio.run(_speak_async(text, voice))
