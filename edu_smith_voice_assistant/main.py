import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from speech_engine import listen, speak, beep, play_alphabet

WAKE_WORDS = ["hello", "hey", "hey anna", "hey edu"]

def contains_wake_word(text):
    return any(word in text.lower() for word in WAKE_WORDS)

class VoiceApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.status_label = Label(text="Listening for 'Hey Edu'...", font_size=24)
        self.add_widget(self.status_label)
        threading.Thread(target=self.background_listener, daemon=True).start()

    def background_listener(self):
        while True:
            self.status_label.text = "Listening for 'Hey Edu'..."
            text = listen()
            print("Wake word check →", text)
            if contains_wake_word(text):
                print("Wake word detected →", text)
                beep()
                self.handle_command()

    def handle_command(self):
        command = listen()
        print("Command received →", command)
        if command:
            if "hello" in command:
                speak("Hello, how can I help you?")
            elif "name" in command:
                speak("My name is Edu, your learning assistant.")
            elif "how are you" in command:
                speak("I'm great! Ready to teach you.")
            elif "time" in command:
                speak("I don't know the time yet, but I will learn soon.")
            elif "alphabet" in command:
                speak("Let's begin learning alphabets.")
                self.status_label.text = "Learning Alphabets..."
                beep()
                play_alphabet()
            else:
                speak("You said: " + command)

class VoiceAppMain(App):
    def build(self):
        return VoiceApp()

if __name__ == "__main__":
    VoiceAppMain().run()
