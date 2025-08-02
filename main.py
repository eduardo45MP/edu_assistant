from modules.voice_input import transcribe_speech
from modules.gpt_client import ask_gpt
from modules.voice_output import speak
from modules.config_loader import load_config

# Load config (from .env + config.json)
CONFIG = load_config()
USER_NAME = CONFIG["user_name"]

def main():
    print(f"👋 Hello, {USER_NAME}. I'm ready to assist you.")
    while True:
        try:
            print("🎤 Listening...")
            user_text = transcribe_speech(CONFIG)

            if not user_text:
                continue

            print(f"🗣️ You said: {user_text}")

            if user_text.lower() in ["exit", "quit", "sair"]:
                print("👋 Bye!")
                break

            response = ask_gpt(user_text)
            print(f"🤖 Assistant: {response}")

            speak(response, CONFIG)

        except KeyboardInterrupt:
            print("\n🛑 Interrupted by user.")
            break

if __name__ == "__main__":
    main()
