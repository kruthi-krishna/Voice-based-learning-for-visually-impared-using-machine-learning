# Voice-based-learning-for-visually-impared-using-machine-learning
It's an user friendly voice assistant similar to bixby,gemini but its an amezing friend how helps visually imaperd people to live a normal life without any hassels.
 Key Features

-  Wake Word Activation 
  Listens for wake phrases like `hello`, `hey`, `hey anna`, or `hey edu` to activate the assistant.

-  Voice-Driven Learning
  Users can say commands like `teach me alphabets` or `teach me numbers` to initiate a spoken learning session.

-  Offline Text-to-Speech 
  Uses offline TTS to ensure the app works without internet connectivity.

-  Interactive Audio Lessons  
  Plays educational audio content (like `alphabets.mp3`) to guide users in a structured way.

-  Cross-Platform GUI 
  Developed with Kivy for desktop applications (Windows/Linux/macOS).

-  Accessibility-Centered Design  
  Tailored for visually impaired children with a fully voice-based interface and no screen navigation.


🧑‍💻 Tech Stack

| Python 3.10+     | Core programming language    
| Kivy             | GUI framework for desktop app 
| SpeechRecognition| Voice input processing       
| pyttsx3          | Offline text-to-speech       
| playsound        | Playback of educational .mp3  
| pyaudio/comtypes | Microphone and speech engine 

Project Structure
edu-smith/
├── main.py # Main GUI app (Kivy + logic)
├── speech_engine.py # Speech-related utilities
├── alphabets.mp3 # Audio file for alphabet learning (custom)
├── numbers.mp3 # Audio file for number learning (custom)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


1. Clone the Repository
git clone https://github.com/kruthi-krishna/edu-smith.git
cd edu-smith

2.Install the dependencies
pip install -r requirements.txt

3.Add files audio file (anything which contains information that needed for the people like lectures/songs/files/notes

4.run the app
python main.py

 Currently working on Future Roadmap
--Add interactive math lessons (addition, subtraction)
-- Introduce quiz-based audio learning
-- Port to Android using Kivy’s mobile support
--Add multi-language support (regional/local dialects)
--Include memory-based revision sessions

Contributions Welcome

Edu Smith is an open-source project aimed at promoting accessible education. We welcome suggestions, bug reports, and feature requests!
Found an issue? Open a GitHub issue.
Got an idea? Create a pull request.
Want to collaborate? Reach out to kruthikrishna30@gmail.com

Acknowledgments

This project is inspired by a commitment to inclusive education and empowering visually impaired learners through AI-powered solutions.
