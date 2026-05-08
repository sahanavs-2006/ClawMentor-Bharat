import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_ai_response(prompt: str, model: str = "llama-3.1-8b-instant") -> str:
    """Generate an AI response using the Groq API."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY environment variable is not set.")
        return "Error: GROQ_API_KEY not configured."
        
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            print(f"Error reaching Groq API (Status {response.status_code}): {response.text}")
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error reaching Groq API: {e}")
        return "Error generating AI response."
