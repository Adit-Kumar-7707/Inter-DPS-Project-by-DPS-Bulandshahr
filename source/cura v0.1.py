import pyttsx3
import datetime
import pywhatkit
import webbrowser
import subprocess
from speech_recognition import *
import speech_recognition as sr
import pyperclip
import random


r = sr.Recognizer()
d = ""


def say(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def stt():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        say("say something")
        print('')
        audio = r.listen(source2)
        say("recognizing the text")
        try:
            global d
            d = r.recognize_google(audio).lower()
            pyperclip.copy(d)
            say("your text is copied")
            commands()
        except:
            say("can you please say it again?")
            pass


def takecommand():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        print('')
        audio = r.listen(source2)
        try:
            global d
            d = r.recognize_google(audio).lower()
        except:
            pass


def takecommand2():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        say("yes i am listening")
        print('')
        audio = r.listen(source2)
        say("recognizing now....")
        try:
            global d
            d = r.recognize_google(audio).lower()
        except:
            pass


def commands():
    say("if you wanna wake me up you can say 'wake'")
    while True:
        takecommand()

        if "bye" in d:
            say("i am going now, have a nice day sir")
            quit()
        elif "wake" in d:
            say("how can i help you sir?")
            takecommand2()
            if "text" in d:
                stt()
                say("okay, now i am runing in background")
            elif "google" in d:
                takecommand2()
                say("searching for")
                say(d)
                pywhatkit.search(d)
                say("okay, now i am runing in background")
            elif "youtube" in d:
                takecommand2()
                say("searching for")
                say(d)
                say("in youtube")
                pywhatkit.playonyt(d)
                say("okay, now i am runing in background")
            elif "entertainment" or "entertain" in d:
                etts()
                say("okay, now i am runing in background")
            elif "code" or "vscode" or "visual" or "studio" in d:
                webbrowser.open("vscode.dev")
                say("okay, now i am runing in background")
            elif "shorts" in d:
                webbrowser.open("https://www.youtube.com/shorts/B84LPO6dk38")
                say("okay, now i am runing in background")
            elif "open" and "youtube" in d:
                webbrowser.open("https://www.youtube.com/")
                say("okay, now i am runing in background")
            elif "git" or "hub" or "github" in d:
                webbrowser.open("https://github.com/")
                say("okay, now i am runing in background")
            elif "calculater" in d:
                subprocess.call("calc.exe")
                say("okay, now i am runing in background")
            elif "notepad" in d:
                subprocess.call("notepad.exe")
                say("okay, now i am runing in background")
        else:
            pass


def searchonyt():
    print("say what you wanna search")
    takecommand2()
    pywhatkit.playonyt(d)
    commands()


def etts():
    etts = ["https://www.youtube.com/watch?v=leFEflp6hSo", "https://www.youtube.com/watch?v=hLQzcLCoCKA", "https://www.youtube.com/watch?v=WWCsGEarExg", "https://www.youtube.com/watch?v=ds2lVJM2viU",
            "https://www.youtube.com/watch?v=hR7jtxbfKvM", "https://www.youtube.com/watch?v=Hf8VenJWAow", "https://www.youtube.com/shorts/B84LPO6dk38", "https://www.youtube.com/shorts/B84LPO6dk38"]
    a = random.choice(etts)
    webbrowser.open(a)


def tut():
    say("if you want any help to operate this program?(say yes/no)")
    while True:
        takecommand2()
        if "yes" in d:
            print('''
            --say "wake" to turn on cura--
            --say "bye" to turn off cura--
            --say "search on youtube" to play a first video in the search of youtube--
            --say "search on google" to search anything on google--
            --say "speech to text" to get a voice's text--
            --say "entertain me" to entertain yourself--
            __to open any app or website__
            just say this - "open <app name>"
            __here app name can be__
            --calculater , cmd , vscode , spotify , office , github , youtube , etc-etc--
            ''')
            say('''
            --say "wake" to turn on cura--
            --say "bye" to turn off cura--
            --say "search on youtube" to play a first video in the search of youtube--
            --say "search on google" to search anything on google--
            --say "speech to text" to get a voice's text--
            --say "entertain me" to entertain yourself--
            __to open any app or website__
            just say this - "open <app name>"
            __here app name can be
            --calculater , cmd , vscode , spotify , github , youtube , etc-etc--
            ''')
            say("okay, now i am runing in background")
            commands()
        elif "no" in d:
            say("okay, now i am runing in background")
            commands()
        else:
            say("say it again")


def onstart():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("good morning , sir")
        say("good morning sir")
    elif hour >= 12 and hour < 16:
        print("good afternoon , sir")
        say("good afternoon sir")
    else:
        print("good evening , sir")
        say("good evening sir")

    print("I am cura, made by ansh , adit and yash")
    say("I am cura, made by ansh , adit and yash")


if __name__ == "__main__":
    onstart()
    tut()
