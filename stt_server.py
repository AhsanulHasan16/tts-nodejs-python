from flask import Flask, request, jsonify
import speech_recognition as sr
from pydub import AudioSegment
import os

app = Flask(__name__)

# Have to set the path to FFmpeg manually
FFMPEG_PATH = r"C:\Users\Saki\Downloads\ffmpeg-2025-02-17-git-b92577405b-full_build\ffmpeg-2025-02-17-git-b92577405b-full_build\bin\ffmpeg.exe"
AudioSegment.converter = FFMPEG_PATH

# Verifing if FFmpeg is being found
if not os.path.exists(FFMPEG_PATH):
    raise FileNotFoundError(f"FFmpeg not found at {FFMPEG_PATH}")


@app.route('/stt', methods=['POST'])
def speech_to_text():
    try:
        data = request.json
        audio_path = data.get('audio_path')
        language = data.get('language', 'en')   # Default language is English

        if not audio_path:
            return jsonify({'error': 'Audio path is required!'}), 400
        
        # Convert audio file to WAV format with 16-bit PCM encoding
        converted_audio_path = "converted_audio.wav"
        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)  # 16-bit PCM format
        audio.export(converted_audio_path, format="wav")

        recongnizer = sr.Recognizer()

        # Load the converted audio file
        with sr.AudioFile(converted_audio_path) as source:
            audio_data = recongnizer.record(source)

        # Convert speech to text using Google Speech Recognition
        text = recongnizer.recognize_google(audio_data, language=language)

        # Delete the converted audio file
        os.remove(converted_audio_path)

        return jsonify({'text': text})  
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)