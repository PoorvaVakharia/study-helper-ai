import os
from dotenv import load_dotenv

load_dotenv()

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")



#def generate_notes(transcript: str) -> str:
#    prompt = f"""
#    Convert the following lecture transcript into:
#    - Bullet-point notes
#    - Clear headings
#    - A short summary at the end
#
#    Transcript:
#    {transcript}
#    """
#
#
#    response = openai.ChatCompletion.create(
#        model="gpt-3.5-turbo",
#        messages=[{"role": "user", "content": prompt}]
#    )
#
#    return response.choices[0].message.content

def generate_notes(transcript: str):
    return {
        "title": "Sample Notes",
        "bullets": [
            "This is a placeholder response",
            "API quota is disabled",
            "Backend pipeline works correctly"
        ]
    }
