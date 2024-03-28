import time

import openai
import pyttsx3
import speech_recognition as sr

# Set up your OpenAI API key
openai.api_key = 'your_api_key_here'


class VoiceController:
    def getOpenAIResponse(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can experiment with different engines
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            stop=None
        )
        return response.choices[0].text.strip()

    def __init__(self, wake_words):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.wake_words = wake_words

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            statement = self.recognizer.recognize_google(audio)
            print(f"User said: {statement}")
            return statement.lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

    def is_wake_word(self, text):
        return any(word in text for word in self.wake_words)

    def dynamicPrompt(user_command):
        return (f"Your name is Ira, you are my home and voice assistant. You are able to control various devices "
                f"throughout my home, including smart plugs, lights, facial recognition cameras that can open doors, "
                f"and much more. I am your boss, and you will address me this way. User said: {user_command}")

    def speakDynamic():
        user_command = takeCommand()
        prompt = dynamicPrompt(user_command)

        # Use OpenAI API for more dynamic responses
        response = getOpenAIResponse(prompt)
        speak(response)
        print(response)

    def speak_dynamic(self, text):
        pass


# Example Usage
if __name__ == "__main__":
    wake_words = ['ira', 'hey ira']  # Add your wake words here
    voice_controller = VoiceController(wake_words)

    while True:
        text = voice_controller.listen()

        if voice_controller.is_wake_word(text):
            voice_controller.speak_dynamic(text)
            time.sleep(2)  # Add a delay to avoid picking up multiple commands in quick succession
