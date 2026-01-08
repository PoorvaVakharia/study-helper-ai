import os
from dotenv import load_dotenv

load_dotenv()

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_notes(transcript: str):
    return {
        "title": "Sample Notes",
        "bullets": [
            "This is a placeholder response",
            "API quota is disabled",
            "Backend pipeline works correctly"
        ]
    }
