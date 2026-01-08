from fastapi import FastAPI, File, UploadFile
from transcribe import transcribe_audio
from notes import generate_notes

# Create the FastAPI application instance
app = FastAPI()


@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    """Endpoint to receive an audio file, transcribe it, and return notes.

    Expects a multipart/form-data POST with a file field. Reads the
    uploaded file into bytes, sends the bytes to the transcription
    helper, then passes the transcript to the notes generator.
    Returns a JSON object with both the transcript and generated notes.
    """
    try:
        # Read the uploaded file contents into memory as bytes
        audio_bytes = await file.read()

        # Convert audio bytes to text using the transcribe helper
        transcript = transcribe_audio(audio_bytes)

        # Generate study notes from the transcript
        notes = generate_notes(transcript)

        # Return the results as JSON
        return {
            "transcript": transcript,
            "notes": notes
        }
    except Exception as e:
        # On error, return a simple error message and a traceback for debugging
        import traceback
        return {"error": str(e), "trace": traceback.format_exc()}
