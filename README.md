# EduAssistant – Personal Voice Assistant with Memory and Local Integration

**EduAssistant** is a fully personalized voice assistant designed to understand your routine, access your local projects, read your calendar, and interact via voice. Built to run locally on your desktop, it seamlessly connects to your digital life while keeping your data private and under your control.

---

## 🔧 Features

- 🎤 Voice input using OpenAI Whisper API (affordable and accurate for short speech)
- 🧠 Interaction powered by GPT-3.5-turbo (low-cost, high-quality language model)
- 🗣️ Voice output using Edge TTS (free, natural-sounding speech synthesis)
- 📁 Smart access to your local files, notes, and personal projects
- 🕓 Basic integration with your personal schedule and routine (via JSON or calendar files)
- 🧾 Lightweight contextual memory: routines, preferences, and task history


---

## 🖥️ Tech Stack

- **Python 3.10+**
- `openai` – access to GPT-3.5-turbo and Whisper API
- `edge-tts` – free, natural-sounding text-to-speech
- `faiss` – vector memory engine (for contextual recall, future feature)
- `python-dotenv`, `requests`, `json` – for config and lightweight integration
- CLI interface (initially), designed to expand into desktop or mobile interface

---

## 📁 Project Structure

```bash
edu_assistant/
├── main.py              # Voice/Text interface
├── config.json          # Personal data and API keys
├── memory/
│   ├── vector_store/    # FAISS storage
│   └── calendar.json    # Calendar data
├── data/
│   └── projects/        # Your organized projects
├── modules/
│   ├── voice_input.py   # Whisper transcription
│   ├── voice_output.py  # Text-to-speech
│   ├── gpt_client.py    # OpenAI API calls
│   ├── context_loader.py # Context generation
│   ├── agenda.py        # Routine and schedule queries
│   └── actions.py       # Automation scripts

````

---

## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:eduardo45MP/edu_assistant.git
   cd edu_assistant
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `config.json` with API keys and personal info.

5. Run the assistant:

   ```bash
   python main.py
   ```

---

## 📌 Roadmap (Short-Term)

* [ ] Stable voice input/output
* [ ] Context awareness via local JSON
* [ ] Google Calendar integration
* [ ] Local file/project interaction
* [ ] Desktop interface
* [ ] Optional offline mode (LLM via Ollama or LM Studio)

---

## 📜 License

MIT – Free to use, modify, and distribute.

---

## ✨ Created by Eduardo, powered by Clara (ChatGPT)
