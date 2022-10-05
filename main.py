import pyttsx3
import datetime
import os
import pywhatkit
import webbrowser
import subprocess
from speech_recognition import *
import speech_recognition as sr
# C:\Users\anshb\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\auto-py-to-exe


def say(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def srtion():
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        print("Listening")
        say("Listening")
        audio = r.listen(source2)
        print("recognizing")
        say("recognizing")

        try:
            d = r.recognize_google(audio)
            print("have you said" , d)
            say("have you said" , d)
        except:
            print("error, you can enter that")
            say("error, you can enter that")

def passw():
    print("password?")
    say("password?")
    a = input().lower()
    if a == "dps":
        pass
    else:
        print("invalid")
        say("invalid")
        passw()


def onStart():
    """
        tells us what to say on start
    """
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



def Whatsapp():
    today = datetime.now()
    shour = today.strftime("%H")
    say("Type Number of Reciever :")
    mobile_no = input("Type Number of Reciever :")
    say("Type Message to send :")
    Msg = input("Type Message to send :")
    say("Write Hour :")
    hour = int(input("Write Hour :"))
    say("Write Minute :")
    minute = int(input("Write Minute :"))
    pywhatkit.sendwhatmsg(mobile_no, Msg, hour, minute)


def prcsslec():
    print("here is some help to operate this program")
    say("here is some help to operate this program")
    print(''' 
Here are some keywords of this Assistant:
1. "whap" or "w" for whatsapp message(only can be used if you have loged in in web.whatsapp.com)
2. "search" or "s" to perform google search
3. "app" or "a" to open any app on this system
4. "soundtotext" or "stt" for converting your voice into text(english only)
5. "q" t quit this program
    ''')
    a = input("write a keyword as written above: ")
    if a == "search" or "s":
        search()
    elif a == 'q':
        quit()
    elif a == "app" or "a":
        open_apps()
    elif a=="stt" or "soundtotext":
        srtion()
    elif a=="q":
        quit()
    elif a=="whap":
        Whatsapp()
    else:
        say("invalid")
        print("invalid")

        



def search():
    say("do you want any help for this? if yes... enter y ,otherwise presh enter")
    c = input("do you want any help for this.. if yes... enter \"y\" ,otherwise presh enter: ")
    if c == 'y':
        print("""
You can write these keywords:
1. "g" for google
2. "y" for Youtube
3. "w" for Whatsapp
4. "s" for Spotify
5. "vc" for VScode
6. "cm" for write your own url(should be full url)
7. "gs" for google search
8. "yt" for youtube
9. "back" to go back to task selector
10. "q" to quit
            """)
    elif c == 'q':
        quit()
    else:
        pass
    while True:
        b = input("write keyword here:")
        if b == "g":
            webbrowser.open("https://www.google.co.in/")
        elif b == 'q':
            quit()
        elif b == "y":
            webbrowser.open("https://www.youtube.com/")
        elif b == "w":
            webbrowser.open("https://web.whatsapp.com/")
        elif b == "s":
            webbrowser.open("https://open.spotify.com/?utm_source=pwa_install")
        elif b == "vc":
            webbrowser.open("https://vscode.dev/")
        elif b == "cm":
            s = input('Full Url:')
            webbrowser.open(s)
        elif b == "yt":
            s = input('Search:')
            pywhatkit.playonyt(s)
        elif b == "gs":
            s = input('Search: ')
            pywhatkit.search(s)
        elif b == 'back':
            prcsslec()
        else:
            print("Invalid")


def open_apps():
    say("do you want any help for this? if yes... enter y ,otherwise presh enter")
    c = input(
        "do you want any help for this.. if yes... enter \"y\" ,otherwise presh enter: ")
    if c == 'y':
        print('''
Here are some Keywords
1. "c" for calculator
2. "note" for notepad
3. "cmd" for cmd
6. "back" to go back to task selector
7. "q" to quit
            ''')
    else:
        pass
    while True:
        b = input('write here:')
        if b == "c":
            subprocess.call("calc.exe")
        elif b == 'q':
            quit()
        elif b == 'back':
            prcsslec()
        elif b == "note":
            subprocess.call("notepad.exe")
        elif b == "cmd":
            subprocess.call("cmd.exe")
        else:
            print("invalid")


if __name__ == "__main__":
    passw()
    while True:
        onStart()
        prcsslec()
