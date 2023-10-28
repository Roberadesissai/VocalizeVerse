import os
import csv
import requests
import shutil

def text_to_speech(text, unique_id, output_dir):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ""
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers, stream=True)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

    output_path = os.path.join(output_dir, f'output{unique_id}.mp3')
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    return output_path

def process_csv_files():
    input_dir = 'Data/Data'
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_dir, file_name)
            output_dir = os.path.join('Output', file_name.split('.')[0])
            os.makedirs(output_dir, exist_ok=True)
            
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                
                # Create a new CSV file in the output directory
                output_csv_path = os.path.join(output_dir, 'output.csv')
                with open(output_csv_path, mode='w', newline='', encoding='utf-8') as out_csvfile:
                    writer = csv.writer(out_csvfile)
                    writer.writerow(['unique_id', 'file_path'])  # Header row

                    for i, row in enumerate(reader):
                        text = row[1]  # Assuming text is in the second column
                        name = file_name.split('.')[0]
                        unique_id = f"{name[:3].upper()}{i:03}"
                        mp3_file_path = os.path.join(output_dir, f'output{unique_id}.mp3')
                        
                        # Check if the file already exists
                        if os.path.exists(mp3_file_path):
                            print(f'File output{unique_id}.mp3 already exists, skipping.')
                            writer.writerow([unique_id, f'output{unique_id}.mp3'])  # Record existing file
                            continue  # Skip to the next iteration
                        
                        mp3_file_path = text_to_speech(text, unique_id, output_dir)
                        writer.writerow([unique_id, f'output{unique_id}.mp3'])

if __name__ == '__main__':
    process_csv_files()
