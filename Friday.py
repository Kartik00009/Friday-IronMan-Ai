import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import winsound
import pygame
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Friday This side. Please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def wakeUp(keyword):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake up keyword...")
        audio = r.listen(source)
    try:
        wake_up_word = r.recognize_google(audio, language='en-in')
        if keyword in wake_up_word:
            speak("Wake up command received")
    except sr.UnknownValueError:
        print("Could not understand audio.")

def setAlarm(alarmTime):
    # Get current time
    currentTime = datetime.datetime.now()
    # Calculate the time difference between the current time and the alarm time
    timeDiff = alarmTime - currentTime
    # Sleep for the time difference
    time.sleep(timeDiff.total_seconds())
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the alarm sound file
    pygame.mixer.music.load("C:\\Users\\User\\Music\\Hum To Dube Hai.mp3")
    # Play the alarm sound
    pygame.mixer.music.play()
    # Wait for the alarm sound to finish
    while pygame.mixer.music.get_busy() == True:
        continue

def takeAlarmCommand():
    speak("Please give the alarm time in format hh:mm")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        hour, minute = query.split(":")
        alarmTime = datetime.datetime.now().replace(hour=int(hour), minute=int(minute), second=0)
        speak(f"Alarm set for {hour}:{minute}")
        setAlarm(alarmTime)
    except Exception as e:
        speak("Could not set alarm")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hello friday' or "hey friday" in query:
            speak("Hello Sir plz tell me how may i help you today")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'set alarm' in query:
            takeAlarmCommand()

        elif 'stop' in query:
                break
