from assistant.voice_control import voice_controller, take_command, wake_words, d
from assistant.devices.lights import control_lights
from assistant.devices.alarms import set_timer, check_timer
from assistant.devices.spotify import control_spotify

def main():
    wish_me()

    while True:
        text = take_command()

        if is_wake_word(text):
            speak_dynamic()

            if "lights" in text:
                control_lights()

            elif "set timer" in text:
                try:
                    minutes = int(text.split("for")[-1].strip())
                    timer_end = set_timer(minutes)
                    speak_dynamic(f"Timer set for {minutes} minutes.")
                    check_timer(timer_end)

                except ValueError:
                    speak_dynamic("Sorry, I couldn't understand the timer duration.")

            elif "spotify" in text:
                action = text.split("spotify ")[-1].lower()
                control_spotify(action)

            # Add more conditions for other features...

            elif "stop" in text or "exit" in text or "quit" in text:
                speak_dynamic("Goodbye boss, have a great day!")
                print("Goodbye boss, have a great day!")
                break

if __name__ == "__main__":
    main()
