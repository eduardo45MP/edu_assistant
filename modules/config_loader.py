import os
import json
from dotenv import load_dotenv

def load_config(config_path="config.json"):
    # Carrega variáveis do .env
    load_dotenv()

    # Tenta carregar config.json (configurações versionadas)
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            json_config = json.load(f)
    except FileNotFoundError:
        json_config = {}

    # Mescla configurações com variáveis de ambiente
    config = {
        # Variáveis sensíveis / ambiente
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "voice_name": os.getenv("VOICE_NAME", "en-US-AriaNeural"),
        "user_name": os.getenv("USER_NAME", "User"),
        "projects_path": os.getenv("PROJECTS_PATH", "./data/projects"),

        # Configurações versionadas
        "use_whisper_api": json_config.get("use_whisper_api", True),
        "timezone": json_config.get("timezone", "America/Sao_Paulo"),
        "calendar_file": json_config.get("calendar_file", "memory/calendar.json"),
        "use_faiss": json_config.get("use_faiss", False),
        "faiss_index_path": json_config.get("faiss_index_path", "memory/vector_store/index.faiss"),
    }

    # Valida chave obrigatória
    if not config["openai_api_key"]:
        raise ValueError("OPENAI_API_KEY missing in environment variables")

    return config
