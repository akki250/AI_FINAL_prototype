import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

import speech_recognition as sr

r = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")
    


    
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Barkha . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=5 )

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
        
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'from wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak('Opening YouTube...')
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak('Opening Google...')
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak('Opening Stack Overflow...')
                webbrowser.open("stackoverflow.com")   

            elif'play music' in query:
                speak('Opening YouTube Music...')
                webbrowser.open("https://music.youtube.com")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            

            # Check if the user said 'stop' or 'cancel'
            elif 'stop' in query or 'cancel' in query:
                speak("Stopping the microphone.")
                break