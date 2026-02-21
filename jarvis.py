import pyttsx3
import speech_recognition as sr
import webbrowser
import pyjokes
import datetime
import os
import wikipedia
import random
import time
import sys

# Speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # show listening
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        print("Recognizing...")  # show recognizing
        try:
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data.lower()
        except:
            print("Not Understand")
            return ""

# Text to speech
def speechtext(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

# Main Jarvis loop
if __name__ == "__main__":
    speechtext("Say Hey Jarvis to activate me")

    while True:
        data = sptext()
        if data == "":
            continue

        # Stop / exit commands
        if any(word in data for word in ["exit", "stop", "quit"]):
            speechtext("Goodbye")
            sys.exit()

        # Wake word detection
        if "hey jarvis" in data:
            speechtext("Yes, I am listening")
            while True:
                command = sptext()
                if command == "":
                    continue

                if any(word in command for word in ["exit", "stop", "quit"]):
                    speechtext("Goodbye")
                    sys.exit()

                elif "your name" in command:
                    speechtext("My name is Jarvis")

                elif "old are you" in command:
                    speechtext("I am a virtual assistant")

                elif "time" in command:
                    time_now = datetime.datetime.now().strftime("%I:%M %p")
                    speechtext(time_now)

                elif "youtube" in command:
                    webbrowser.open("https://www.youtube.com/")
                    speechtext("Opening YouTube")

                elif "search" in command:
                    speechtext("What should I search?")
                    query = sptext()
                    if query:
                        webbrowser.open(f"https://www.google.com/search?q={query}")
                        speechtext("Here are the results")

                elif "joke" in command:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    speechtext(joke)

                elif "play song" in command:
                    path = r"C:\Users\UNIQUE COMPUTER\Desktop\vedio"
                    if os.path.exists(path):
                        songs = os.listdir(path)
                        if songs:
                            song = random.choice(songs)
                            os.startfile(os.path.join(path, song))
                            speechtext("Playing song")
                        else:
                            speechtext("No songs found in the folder")
                    else:
                        speechtext("Song folder not found")

                # Wikipedia knowledge queries
                elif "tell me about" in command or "who is" in command or "what is" in command:
                    speechtext("Searching...")
                    topic = command.replace("tell me about", "").replace("who is", "").replace("what is", "").strip()
                    try:
                        results = wikipedia.search(topic)
                        if results:
                            page = results[0]
                            info = wikipedia.summary(page, sentences=2)
                            print(info)
                            speechtext(info)
                        else:
                            speechtext("Sorry, I could not find information on that topic")
                    except:
                        speechtext("Sorry, I could not find information on that topic")

                time.sleep(1)