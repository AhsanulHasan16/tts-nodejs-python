import express, { application } from 'express';
import { PythonShell } from 'python-shell';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 5000;

app.use(express.json());


app.get('/', (req, res) => {
  res.send('Hello World! This is my new express server with Python!');
});


// API for the TTS part
app.post('/tts', (req, res) => { 

    const { text, voice } = req.body;

    if (!text) {
        return res.status(400).json({ message: 'Text is required!' });
    }

    const selectedVoice = voice === "male" ? "male" : "female";

    let options = {
        mode: 'text',
        pythonOptions: ['-u'],  // Unbuffered output
        args: [text, selectedVoice]
    }

    PythonShell.run('tts.py', options).then(results => {
        console.log(`Python Output: ${results}`);
        res.download(path.join(__dirname, 'output.mp3'));     // Sending the generated audio file to the client!
    }).catch(err => {
        console.error('Python script error: ', err);
        res.status(500).json({ message: 'Failed to generate speech!' });
    });
});


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});