from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)


@app.route('/stt', methods=['POST'])
def speech_to_text():
    try:
        data = request.json
        audio_path = data.get('audio_path')

        if not audio_path:
            return jsonify({'error': 'Audio path is required!'}), 400
        
        recongnizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(audio_path) as source:
            audio_data = recongnizer.record(source)

        # Convert speech to text using Google Speech Recognition
        text = recongnizer.recognize_google(audio_data, language="en")

        return jsonify({'text': text})  
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)