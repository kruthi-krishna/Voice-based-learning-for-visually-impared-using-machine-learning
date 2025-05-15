# Voice-Based AI Learning Assistant for the Visually Impaired

This is a Kivy-based voice assistant app that helps visually impaired children learn using voice commands.

## Features

- Wake word detection (e.g., "Hey Edu")
- Voice command handling
- Alphabet learning via audio
- Text-to-speech feedback

## Tech Stack

- Python
- Kivy
- SpeechRecognition
- pyttsx3
- playsound

## How to Run

1. Install dependencies:
    ```bash
    pip install kivy SpeechRecognition pyttsx3 playsound
    ```

2. Place `beep.mp3` and `alphabets.mp3` in the root folder.

3. Run the app:
    ```bash
    python main.py
    ```

## Notes

- Make sure you have a working microphone.
- Test wake word detection and audio response.
