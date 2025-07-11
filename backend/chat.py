import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_video(video_id: str, question: str) -> str:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi', 'en'])
        if not transcript:
            return "Transcript not available for this video."
        transcript_text = " ".join([entry["text"] for entry in transcript])
        prompt = f"""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say context not available in the video Also return the output in Only English.
        

        Transcript:
        {transcript_text}

        Question: {question}
        """
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        if hasattr(response, "error") and response.error:
            return f"Error: {response.error.message}"
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
# print(chat_with_video("Gfr50f6ZBvo", "What is the video about?"))