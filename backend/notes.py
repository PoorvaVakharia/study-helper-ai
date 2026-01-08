import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()

import openai

# Configure OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_notes(transcript: str):
    """Generate study notes from a transcript string.

    Currently returns a placeholder dictionary. In a full implementation
    this function would call the OpenAI API (or other NLP tools) to
    create structured notes from the transcript text.
    """
    return {
        "title": "Sample Notes",
        "bullets": [
            "This is a placeholder response",
            "API quota is disabled",
            "Backend pipeline works correctly"
        ]
    }
