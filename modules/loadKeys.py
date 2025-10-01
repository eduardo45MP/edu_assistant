import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class APIKeys:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.validate()
        self.client = OpenAI(api_key=self.openai_api_key)
        print(f"🔑 Using API key: {self.openai_api_key}")


    def validate(self):
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in .env")

    def get_openai_client(self):
        return self.client

keys = APIKeys()

