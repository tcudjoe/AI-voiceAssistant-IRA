import speech_recognition as sr
import pyttsx3
import time


class VoiceController:
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

    def dynamic_prompt(self, user_command):
        return (f"Your name is Ira, you are my home and voice assistant. You are able to control various devices "
                f"throughout my home, including smart plugs, lights, facial recognition cameras that can open doors, "
                f"and much more. I am your boss, and you will address me this way. User said: {user_command}")

    def speak_dynamic(self, user_command):
        prompt = self.dynamic_prompt(user_command)
        response = get_openai_response(prompt)  # Assume you have a function to get OpenAI response
        self.speak(response)


# Example Usage
if __name__ == "__main__":
    wake_words = ['ira', 'hey ira']  # Add your wake words here
    voice_controller = VoiceController(wake_words)

    while True:
        text = voice_controller.listen()

        if voice_controller.is_wake_word(text):
            voice_controller.speak_dynamic(text)
            time.sleep(2)  # Add a delay to avoid picking up multiple commands in quick succession
