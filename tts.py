import sys
import pyttsx3
from gtts import gTTS
import os

def text_to_speech(text, voice, language):
    if language == "bn":
        tts = gTTS(text=text, lang='bn')
        tts.save("output.mp3")
    else:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if voice == "male":
            engine.setProperty('voice', voices[0].id)   # Male voice
        else:
            engine.setProperty('voice', voices[1].id)   # Female voice. Default one.

        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()

    print('Text to speech conversion done!')

if __name__ == '__main__':
    text = sys.argv[1]      # Getting the text from Node.js
    voice = sys.argv[2] if len(sys.argv) > 2 else "female"    # Getting the voice from Node. Default is female.
    language = sys.argv[3] if len(sys.argv) > 3 else "en"    # Getting the language from Node. Default is english.
    text_to_speech(text, voice, language)