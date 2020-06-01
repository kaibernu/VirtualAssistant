import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang='en')#pt-br
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("Hello. What's your name?")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

name = get_audio() 

speak("Hello {}. How are you?".format(name))
text = get_audio()

while text != "I'm fine":
    speak("Hello {}. How are you?".format(name))
    text = get_audio()
    if "I'm fine" in text:
        speak("great. I'm happy for you {}".format(name))
        break
    elif "fine" in text:
        speak("great. I'm happy for you {}".format(name))
        break
    else:
        speak("I didn't understand")
else :
    speak("great. I'm happy for you {}".format(name))
           
    
speak("Nice to meet you!{}".format(name))
text = get_audio()
if "nice to meet you too" in text:
    speak("Thank you ")
else:
    speak("I didn't understand")