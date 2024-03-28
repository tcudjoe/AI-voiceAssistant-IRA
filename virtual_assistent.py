from urllib import response
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
# import wolframalpha
import requests

# ignore any warning message
warnings.filterwarnings("ignore")

hour = datetime.datetime.now().hour

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    if hour >= 0 and hour < 12:
        speak("Good morning boss")
        print("Good morning boss")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon boss")
        print("Good afternoon boss")
    else:
        speak("Good evening boss")
        print("Good evening boss")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio)
            print("user said:{statement}\n")
        except sr.UnknownValueError:
            print("google speech recognition could not understand")
        except Exception as e:
            speak("Could you repeat that again, please?")
            # return "none"
        return statement

def wakeWord(text):
    WAKE_WORDS = ['hey ira', 'okay ira', 'ira', 'goodmorning ira', 'good afternoon ira', 'good evening ira']
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today
    weekday = calendar.Calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

# print("listening IRA")
# speak("Loading eira")
# wishMe()
# wake_word = "hey ira"

if __name__ == "__main__":
    while True:
        text = takeCommand()
        response = ''

        if (wakeWord(text) == True):
            wishMe()
            speak("Tell me, how can i help you?")

            if text == 0:
                continue
            # if "bye" in text or "thank you" in text or "shutdown" in text or "goodbye" in text or "shutdown please" in text or "you can go" or " you can shutdown" in text:
            #     if hour >= 0 and hour < 12:
            #         speak("Goodbye boss, have a wonderful morning!")
            #         print("Goodbye boss, have a wonderful morning!")
            #         takeCommand()
            #     elif hour >= 12 and hour < 18:
            #         speak("Goodbye boss, have a wonderful afternoon!")
            #         print("Goodbye boss, have a wonderful afternoon!")
            #         takeCommand()

            #     else:
            #         speak("Goodbye boss, have a wonderful evening!")
            #         print("Goodbye boss, have a wonderful evening!")
            #         takeCommand()

            if "time" in text:
                now = datetime.datetime.now
                if now.hour >= 12:
                    hour = now.hour
                    if now.minute < 10 :
                        minute = '0'+str(now.minute)
                    else:
                        minute = str(now.minute)

                speak(' ' + 'it is ' + str(hour) + ':' + minute + ' ' + ' .')

        # speak(response)
