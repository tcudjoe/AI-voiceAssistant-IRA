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

hour = datetime.datetime.now().hour

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()

def speak(text):
    engine.say(text)
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
        # print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language='eng-in')
            print(said)
        # except Exception as e:
        #     print("Exception: " + str(e))

        except Exception as e:
            speak("Could you repeat that again, please?")
            return "none"
        return said.lower()

def Wake(text):
    Wake_Words = ['hey ir-ruh', 'goodmorning ir-ruh', 'good afternoon ir-ruh', 'good evening ir-ruh', 'ir-ruh']
    text = text.lower()

    # for phrase in Wake_Words:
    #     if phrase in text:
    #         return True
    # return 0

# print("Loading IRA")
# speak("Loading  ir-ruh")

if __name__ == "__main__":
    while True:
        print('listening')
        text = takeCommand()

        if text.count(Wake) > 0:
            wishMe()
            text = takeCommand()

            speak("Tell me, how can i help you?")

            statement = takeCommand().lower()
            if statement == 0:
                continue
            if ["bye", "thank you", "shutdown", "goodbye", "shutdown please", "you can go", "you can shutdown"] in statement:
                if hour >= 0 and hour < 12:
                    speak("Goodbye sir, have a wonderful morning!")
                    print("Goodbye sir, have a wonderful morning!")
                    print('waiting for your next command...')
                elif hour >= 12 and hour < 18:
                    speak("Goodbye sir, have a wonderful afternoon!")
                    print("Goodbye sir, have a wonderful afternoon!")
                    print('waiting for your next command...')
                else:
                    speak("Goodbye sir, have a wonderful evening!")
                    print("Goodbye sir, have a wonderful evening!")
                    print('waiting for your next command...')

        # if (Wake(text) == true):

