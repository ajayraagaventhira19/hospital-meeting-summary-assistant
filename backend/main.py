from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Hospital Meeting Summary API Running"}

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # dummy response for week 1
    return {
        "transcript": "This is dummy transcript from uploaded meeting audio.",
        "summary": "Doctors discussed hospital management improvements.",
        "status": "success"
    }
