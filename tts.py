import sys
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    print('Text to speech conversion done!')

if __name__ == '__main__':
    text = sys.argv[1]      # Getting the text from Node.js
    text_to_speech(text)