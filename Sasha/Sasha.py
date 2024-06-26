import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ecapture
import json
from urllib.request import urlopen
import wolframalpha
try:
    client = wolframalpha.Client("64TY6Q-RPLX9JTKK4")
except Exception:
    print("internet connection failed")
   


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello boss, i'm Sasha. How can i help you? ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('ujjwal2104cse@gemspolytechnic.edu.in', '#')
    server.sendmail('ujjwalraj8935@gmail.com', to, content)
    server.close()





if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query or 'play song'in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query or "open visual studio" in query:
            codePath= "C:\\Users\\ujjwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "camera" in query or "take a photo" in query or "take a selfie" in query:
            ecapture.capture(0, "Jarvis Camera ", "img.jpg")

        elif "who are you" in query:
            speak("I am your advanced virtual assistant created by Team Tera Baap")

        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=4c6fd3c9a0754c898d9c70d3d2e41a7b''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'email to ujjwal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ujjwalraj8935@gmail.com"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "say sorry" in query:
            speak("i'm sorry palak, forgive me, you are my cutest sister")

        else:
            try:
                query = query.replace("sasha", "")
                res = client.query(query)
                output = next(res.results).text
                speak(next(res.results).text)
                print(next(res.results).text)
            except Exception:
                print("internet connection failed")
                speak("internet connection failed")



        


        