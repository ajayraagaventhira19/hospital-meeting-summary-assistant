# Hospital Meeting Summary Assistant

## Project Code
PRJ-020

## Project Description
This project helps hospitals summarize staff meeting discussions.

The system allows users to:
- Upload meeting audio
- Convert speech to text
- Generate meeting summary
- Extract action items
- Download reports

## Tech Stack
- Python
- FastAPI
- Streamlit
- Transformers
- Whisper
- FPDF

## Week 1 Progress
✅ Project setup completed  
✅ FastAPI backend created  
✅ Streamlit frontend created  
✅ Audio upload working  
✅ Dummy summary output working  

## Folder Structure

hospital-summary/
│
├── backend/
├── frontend/
├── uploads/
├── reports/
└── README.md

## How to Run

### Backend
```bash
cd backend
uvicorn main:app --reload
