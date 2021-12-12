# Description: This, IRA, is my OWN virtual assistent program that gets the time, the date, responds with a greeting,
#              returns information from the internet and much more that we might be making at a later stadium.


#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

import speech_recognition as sr
import os
import pyttsx3
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import datetime
import time
import webbrowser
import wolframalpha
import requests

# ignore any warning message
warnings.filterwarnings("ignore")

hour=datetime.datetime.now().hour

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    if hour >= 0 and hour < 12:
        speak("Good morning sir")
        print("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
        print("Good afternoon sir")
    else:
        speak("Good evening sir")
        print("Good evening sir")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='eng-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Could you repeat that again, please?")
            return "none"
        return statement

def Wake(text):
    Wake_Words = ['hey eira', 'goodmorning eira', 'good afternoon eira', 'good evening eira']
    text = text.lower()

    for phrase in Wake_Words:
        if phrase in text:
            return True
    return 0

print("Loading IRA")
speak("Loading eira")
wishMe()

if __name__ == "__main__":
    while True:
        speak("Tell me, how can i help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if "bye" in statement or "thank you" in statement or "shutdown" in statement or "goodbye" in statement or "shutdown please" in statement or "you can go" or " you can shutdown" in statement:
            if hour >= 0 and hour < 12:
                speak("Goodbye sir, have a wonderful morning!")
                print("Goodbye sir, have a wonderful morning!")
                break
            elif hour >= 12 and hour < 18:
                speak("Goodbye sir, have a wonderful afternoon!")
                print("Goodbye sir, have a wonderful afternoon!")
                break
            else:
                speak("Goodbye sir, have a wonderful evening!")
                print("Goodbye sir, have a wonderful evening!")
                break

        # if (Wake(text) == true):

