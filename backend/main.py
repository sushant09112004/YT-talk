from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from chat import chat_with_video
from pydantic import BaseModel

app = FastAPI()

# Allow frontend (popup.js) to call backend - using wildcard for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
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
    try:
        if not request.video_id:
            raise HTTPException(status_code=400, detail="Video ID is required")
        if not request.question:
            raise HTTPException(status_code=400, detail="Question is required")
        
        answer = chat_with_video(request.video_id, request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
