import requests
import os
import json
import csv

# Constants
CHUNK_SIZE = 1024
API_URL = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream"
HEADERS = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ""
}
OUTPUT_BASE_DIR = 'VoiceResponses'

def text_to_speech(text, output_path):
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(API_URL, json=data, headers=HEADERS, stream=True)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

def generate_voice_responses(data):
    for waking_name, responses in data["WakingNameResponses"].items():
        output_dir = os.path.join(OUTPUT_BASE_DIR, waking_name.replace(' ', '_'))
        os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
        output_csv_path = os.path.join(output_dir, 'output.csv')
        
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as out_csvfile:
            writer = csv.writer(out_csvfile)
            writer.writerow(['response_text', 'file_path'])
            
            for i, response_text in enumerate(responses):
                file_name = f'response_{i}.mp3'
                output_path = os.path.join(output_dir, file_name)
                if not os.path.exists(output_path):
                    text_to_speech(response_text, output_path)
                writer.writerow([response_text, output_path])

# Read the JSON data from a file
with open('WakingNameResponse.json', 'r') as file:
    data = json.load(file)

# Call the function to generate voice responses
generate_voice_responses(data)
