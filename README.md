# 🎙️ YT-Talk Chrome Extension

This project is a Chrome extension integrated with an AI backend (powered by Gemini) that helps users interact with YouTube video content more intelligently. It extracts the transcript of the currently playing video and uses AI to answer user questions based on that content.

---

## 🚀 Features

- Chrome Extension to fetch current YouTube video ID
- FastAPI backend to process video transcripts
- AI-powered Q&A using Gemini
- Real-time transcript chunking and smart querying

---

## 🗂 Project Structure

│
├── backend/
│ ├── main.py
│ ├── chat.py
│ ├── test_backend.py
│ ├── pycache/
│ └── venv/
│
├── extension/
│ ├── popup.html
│ ├── popup.js
│ └── manifest.json
│
└── README.md



---

## 🧪 Requirements

Make sure you have the following installed:

- Python 3.10+
- Google Chrome (for extension)
- Node.js (if you plan to bundle/serve frontend)
- A valid Gemini API key (used in backend)

---

## 🛠 How to Run the Backend (FastAPI)

1. **Navigate to the backend folder**:
   ```bash
   cd backend
python -m uvicorn main:app --reload --port 8000
