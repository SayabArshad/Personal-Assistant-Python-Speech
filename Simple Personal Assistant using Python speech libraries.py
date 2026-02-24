#import libraries
#pip install SpeechRecognition
#pip install pyttsx3
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant:", text)

# Function to listen to user commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("User:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""
    
# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your personal assistant. How can I help you today?")

# Main function to run the assistant
def main():
    greet()
    while True:
        command = listen()
        
        if 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        
        elif 'what time is it' in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}.")
        
        elif 'play music' in command:
            music_dir = 'C:\\Path\\To\\Your\\Music\\Directory'  # Change this to your music directory
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                speak(f"Playing {song}.")
            else:
                speak("No music files found in the directory.")
        
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I am sorry, I can't perform that task yet.")
        
if __name__ == "__main__":
    main()
    