import pyttsx3
engine = pyttsx3.init()

if __name__ == '__main__':

    engine.say("Welcome to RoboSpeaker 1.1. Created by Rahul")
    engine.runAndWait()
    while True:
        x = input("Enter what you want me to speak: ")
        if x== "q":
            engine.say("bye bye friend'")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
