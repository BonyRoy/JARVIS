import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif 12 >= hour and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 20:
        speak("Good Evening Sir")

    speak("I am Clement Sir. Please tell me how may i help you")


def takecommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: (query)\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        #speak("Say that again please....")
        return "None"
    return query

def talk(audio):
    pass


if __name__ == "__main__":
    wishMe()
    while True:

        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        #elif "play music" in query:
            #music_dir = ""
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif "open pycharm" in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif "open unity" in query:
            codePath = "C:\\Program Files\\Unity\Hub\Editor\\2019.4.18f1\\Editor\\Unity.exe"
            os.startfile(codePath)

        elif "open solidworks" in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\SOLIDWORKS 2019"
            os.startfile(codePath)


        elif "open Microsoft Word" in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"
            os.startfile(codePath)


        elif "open Arduino Ide" in query:
            codePath = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(codePath)

        elif "open Microsoft Powerpoint" in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        #elif 'send email to sd' in query:
            #try:
               # speak("what should i say?")
               # content = takecommand()
               # to = "siddhantroy80ny@gmail.com"
              #  sendEmail(to, content)
              #  speak("Email has been sent")
            #except Exception as e:
               # print(e)
               # speak("Sorry roy sir i am not able to send this email")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={cm}")

        elif "open youtube" in query:
            speak("sir,what should i search on youtube")
            x = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")


        elif "open meet" in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com//")

        elif "play song on cloud" in query:
            speak("tell me the song name!")
            p = takecommand()
            webbrowser.open(f"https://soundcloud.com//search?q={p}")

        elif "open command prompt" in query:
            os.system('start cmd')

        elif "why you came to world" in query:
            speak("thanks to ROY ,in order to make his life more easier with artificial intelligence")


        elif "your name" in query:
            speak("Thanks for Asking my name, my self clement")

        elif 'date' in query:
            speak('sorry, i have a headache')

        elif 'are you single' in query:
            speak('i have a relationship with wifi')

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'break fast' in query:
            speak('i am a an assistant i get energy from internet sir')

        elif 'owner' in query:
            speak('ROY')

        elif 'who made' in query:
            speak("ROY made me for someone special")

        elif 'How are you' in query:
            speak('i am fine \n how are you sir')

        elif 'Hi' in query:
            speak('hello , how are you ')

        elif 'fine' in query:
            speak('great to hear that')

        elif "exit" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif "good morning" or "good afternoon" or "good evening " or "good night" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning Sir")
            elif 12 >= hour and hour < 18:
                speak("Good Afternoon Sir")
            elif hour >= 18 and hour < 20:
                speak("Good Evening Sir")
            else:
                speak("Good Night sir")

            speak("I am Clement Sir. Please tell me how may i help you")

        elif "tell about ypurself" or "who are you" in query:
            speak('''myself Clement i was born on 18th March 2021 ...\n My sir ROY made me \n 
            i am a assistant to perform small task ''')


