import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Speech services {0}".format(e))

    return(data)

def jarvis(data):
    if "how are you" in data:
        speak("I am fine.")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on while I show you where " + location + " is.")
        os.system("chrome https://www.bing.com/maps/place/" + location +"/&amp;")


time.sleep(2)
speak("Hi what can i do for you?")
while 1:
    data = recordAudio()
    jarvis(data)

    
        
