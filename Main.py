import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import os

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir!")
    speak("Hi Sir Welcome back jarvis is ready")
    speak("HOW CAN I HELP YOU")


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Pleasw wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except Exception as ex:
        print(ex)
    if 'chrome'in text:
        a='Opening chrome..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    if 'firefox'in text:
        a='Opening firefox..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Mozilla Firefox\Firefox.exe"
        subprocess.Popen([programName])
    if 'open youtube in firefox'in text:
        a='Opening youtube..'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Mozilla Firefox\Firefox.exe"
        fileName = "www.youtube.com"
        subprocess.Popen([programName,fileName])
    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    if 'how are you' in text:
        speak("Absolutely Fine sir! MY operating System is completely good")
    if 'hi jarvis' in text:
        speak("Hi sir how can i help you!")
wishMe()
while True:
    cmd()
