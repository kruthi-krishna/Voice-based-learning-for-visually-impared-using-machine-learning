import speech_recognition as sr
import pyttsx3
import os
from playsound import playsound

engine = pyttsx3.init()

def speak(text):
    print("Speaking →", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("Recognized →", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out")
            return ""
        except sr.RequestError:
            print("Speech recognition service failed")
            return ""

def beep():
    try:
        playsound("beep.mp3")
    except Exception as e:
        print("Beep sound failed:", e)

def play_alphabet():
    try:
        playsound("alphabets.mp3")
    except Exception as e:
        print("Alphabet sound failed:", e)
