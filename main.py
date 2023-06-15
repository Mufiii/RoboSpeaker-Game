
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.1 Created By Mufees")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak ('q' to quit): ")
        if x == 'q':
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        try:
            engine.say(x)
            engine.runAndWait()
        except Exception as e:
            print("Error occurred during text-to-speech conversion:", str(e))


