import express, { application } from 'express';
import { PythonShell } from 'python-shell';
import path from 'path';
import { fileURLToPath } from 'url';
import multer from 'multer';
import axios from 'axios';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 5000;

app.use(express.json());


// Multer configuration for audio file uploads
const upload = multer({ dest: 'uploads/' });


app.get('/', (req, res) => {
  res.send('Hello World! This is my new express server with Python!');
});

// API for the TTS part
app.post('/tts', (req, res) => { 

    const { text, voice, language } = req.body;

    if (!text) {
        return res.status(400).json({ message: 'Text is required!' });
    }

    const selectedVoice = voice === "male" ? "male" : "female";
    const selectedLanguage = language === "bn" ? "bn" : "en";

    let options = {
        mode: 'text',
        pythonOptions: ['-u'],  // Unbuffered output
        args: [text, selectedVoice, selectedLanguage]
    }

    PythonShell.run('tts.py', options).then(results => {
        console.log(`Python Output: ${results}`);
        res.download(path.join(__dirname, 'output.mp3'));     // Sending the generated audio file to the client!
    }).catch(err => {
        console.error('Python script error: ', err);
        res.status(500).json({ message: 'Failed to generate speech!' });
    });
});


// API for the STT part
app.post('/stt', upload.single('audio'), async (req, res) => {

    try {
        if (!req.file) {
            return res.status(400).json({ message: 'Audio file is required!' });
        }

        const audioFilePath = path.join(__dirname, req.file.path);
        console.log('Audio File Path: ', audioFilePath);

        // Sending the audio file path to the python server
        const response = await axios.post('http://localhost:5001/stt', { 
            audio_path: audioFilePath
        });

        fs.unlinkSync(audioFilePath);    // Deleting the audio file after use

        console.log("Response from STT API: ", response.data.text);

        res.json({ text: response.data.text });

    } catch (error) {
        console.error('STT API error: ', error);
        res.status(500).json({ message: 'Failed to convert speech to text!' });
    }

});


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});