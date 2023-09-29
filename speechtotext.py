import os
import tempfile
import speech_recognition as sr
import requests
import pyttsx3
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Debug: print available Microphones
        print("Available Microphones:", sr.Microphone.list_microphone_names())

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    return text