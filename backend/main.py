from fastapi import FastAPI, File, UploadFile
from transcribe import transcribe_audio
from notes import generate_notes

app = FastAPI()

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    try:
        audio_bytes = await file.read()
        transcript = transcribe_audio(audio_bytes)
        notes = generate_notes(transcript)
        return {
            "transcript": transcript,
            "notes": notes
        }
    except Exception as e:
        # Return the actual error for debugging
        import traceback
        return {"error": str(e), "trace": traceback.format_exc()}
