from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chat import chat_with_video
from pydantic import BaseModel

app = FastAPI()

# Allow frontend (popup.js) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://ldibomgoniehalhpcgdnbkflfggokgkf"],  # Replace with extension origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    video_id: str
    question: str

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    return {"answer": chat_with_video(request.video_id, request.question)}
