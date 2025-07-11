import requests
import json

def test_backend():
    # Test the root endpoint
    try:
        response = requests.get("http://localhost:8000/")
        print(f"Root endpoint test: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Root endpoint test failed: {e}")
        return False

    # Test the chat endpoint
    try:
        test_data = {
            "video_id": "dQw4w9WgXcQ",  # Rick Roll video ID for testing
            "question": "What is this video about?"
        }
        
        response = requests.post(
            "http://localhost:8000/chat",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data)
        )
        
        print(f"Chat endpoint test: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {result.get('answer', 'No answer')[:100]}...")
        else:
            print(f"Error response: {response.text}")
            
    except Exception as e:
        print(f"Chat endpoint test failed: {e}")
        return False

    return True

if __name__ == "__main__":
    print("Testing backend...")
    test_backend() 