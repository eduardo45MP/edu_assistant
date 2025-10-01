import os
import tempfile
import sounddevice as sd
from scipy.io.wavfile import write
from .loadKeys import keys  # singleton instance
import openai

def record_audio(duration=5):
    default_input = sd.default.device[0]  # Get default input device
    info = sd.query_devices(default_input, 'input')
    samplerate = info['default_samplerate']
    print("🎙️ Speak now...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return audio, samplerate

def transcribe_speech(config):
    use_api = config.get("use_whisper_api", True)

    if not use_api:
        print("❌ Local Whisper not implemented yet.")
        return ""

    client = keys.get_openai_client()
    audio, samplerate = record_audio()
    samplerate = int(samplerate)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        write(tmpfile.name, samplerate, audio)
        audio_path = tmpfile.name

    try:
        print("📡 Sending audio to Whisper API...")
        with open(audio_path, "rb") as f:
            transcript = client.audio.transcriptions.create(
                file=f,
                model="whisper-1"
            )
        return transcript.text.strip()

    except Exception as e:
        print(f"❗ Transcription error: {e}")
        return ""

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)
