from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        return f"Transcript fetch error: {str(e)}"
