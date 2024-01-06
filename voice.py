import speech_recognition as sr


import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
 
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Error accessing Google Speech Recognition service: {e}")
        return ""

def main():
    speak("Hello! I'm your voice assistant. How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
