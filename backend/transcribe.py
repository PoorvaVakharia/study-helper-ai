import whisper
import tempfile
import warnings

# Suppress a harmless warning when running Whisper on CPU-only machines
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")


# Load the Whisper model once at module import time (small 'base' model)
model = whisper.load_model("base")


def transcribe_audio(audio_bytes: bytes) -> str:
    """Write audio bytes to a temp file and transcribe using Whisper.

    The function returns the transcription text. Using a temporary file
    keeps the API simple (Whisper expects a filename) and avoids storing
    audio permanently on disk.
    """
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp:
        # Write the uploaded bytes to the temp file and ensure it's flushed
        tmp.write(audio_bytes)
        tmp.flush()

        # Run Whisper transcription on the temporary file
        result = model.transcribe(tmp.name)
        return result["text"]
