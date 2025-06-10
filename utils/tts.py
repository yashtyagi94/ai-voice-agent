import requests, os
from dotenv import load_dotenv

load_dotenv()

def speak(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = "Xb7hH8MSUJpSbSDYk0k2"  # Replace with your actual voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",  # Optional, can also use "eleven_multilingual_v1"
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")

    audio_path = "response_audio.mp3"
    with open(audio_path, 'wb') as f:
        f.write(response.content)

    return audio_path
