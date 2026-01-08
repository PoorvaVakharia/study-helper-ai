const uploadBtn = document.getElementById('uploadBtn');
const audioFileInput = document.getElementById('audioFile');
const transcriptEl = document.getElementById('transcript');
const notesEl = document.getElementById('notes');

uploadBtn.addEventListener('click', async () => {
    const file = audioFileInput.files[0];
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    transcriptEl.textContent = "Uploading...";
    notesEl.textContent = "";

    try {
        const res = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (data.error) {
            transcriptEl.textContent = "Error: " + data.error;
            notesEl.textContent = data.trace || "";
        } else {
            transcriptEl.textContent = data.transcript;
            notesEl.textContent = data.notes;
        }
    } catch (err) {
        transcriptEl.textContent = "Network error: " + err;
    }
});
