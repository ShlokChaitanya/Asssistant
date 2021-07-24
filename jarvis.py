
import audioop
from math import e
import random
import sys
from typing import Any
from pyjokes.pyjokes import get_joke
import pyttsx3
import os 
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hare Krishna ")               
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")

    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")

    else:
         speak("Good Evening!")
 
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='hindi') 
        print(f"User said: {query}\n")  

    except Exception as e:
        print("Say that again please...") 
        return "None" 
    return query       

    
if __name__ ==  "__main__" :
    wishMe()
    query = takecommand().lower()

    if 'search' in  query:
        speak('Searching ....')
        query = query.replace("searching","")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)

    elif 'open amazon' in query:
        speak("Opening Amazon!")
        webbrowser.open("amazon.in")

    elif 'open youtube' in query:
        speak("Opening YouTube!")
        webbrowser.open("youtube.com")

    elif 'tell a joke' in query:
        joke = pyjokes.get_joke(language='en', category='neutral')
        speak(joke)
        print(joke)    

    elif ' open google' in query:
        speak("Opening Google!")
        webbrowser.open("google.com")
    
    elif ' open chrome' in query:
        speak("Opening Chrome!")
        Chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
        os.startfile(Chromepath) 

    elif 'open brave' in query:
        speak("Opening Brave!")
        BravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(BravePath)        

    elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" The time is {strTime}") 

    elif 'open whatsapp' in query:
        speak('Opening Whatsapp')  
        webbrowser.open("web.whatsapp.com")                  

    elif 'play music' in query:
            music_dir = 'E:\Scans\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'open vedabase' in query:
        speak("Opening Vedabase!")
        webbrowser.open("vedabase.io")

    elif 'iskcon delhi live' in query:
        speak("Opening Iskcon Delhi Live")
        webbrowser.open("youtube.com/iskcondelhitv")
        
    elif 'play song' in query:
            music_dir = 'E:\\Scans\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))    

    elif ' open zoom' in query:
        speak("Opening Zoom")
        zoompath="C:\\Users\\Rishi kumar\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"        
        os.startfile(zoompath)

    elif 'close zoom' in query:
        speak("Closing Zoom")        
        os.system("taskkill /f/im Zoom.exe")

    elif 'open mobile photo' in query:
        speak("Opening Mobile photo")
        photoPath = "C:\\Users\\Rishi kumar\\Desktop\\Mobile photo"
        os.startfile(photoPath) 

    elif 'open google' in query:
        speak('what should i search on google')
        webbrowser.open(f'{query}')

    elif 'thank you' in query:
        speak('thank you, have a good day')

    elif 'set alarm' in query:
        alarm = int(datetime.datetime.now().hour())
        if alarm==22:
            music_dir='E:\\Scans\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))    
    
    elif 'youtube' in query:
        speak('searching on youtube')
        cm = takecommand().lower()
        webbrowser.open(f'www.youtube.com{cm}')

    elif 'turn on ac' in query:
        speak('bijili ka bill tera baaap bhaaraega')    

    elif 'turn off ac' in query:
        speak('room thandaa hone de')

    elif 'tell me weather' in query:
        speak('khadki khuli hai')
                