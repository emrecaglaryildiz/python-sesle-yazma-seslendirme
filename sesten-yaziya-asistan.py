import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit=sr.Recognizer()

def dinleme (a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon=kayit.listen(kaynak)
        ses=""

        try:
            ses=kayit.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan anlayamadı..")
        except sr.RequestError:
            print("Asistan çalışmıyor..")

        return ses

print("Sistem aktif, Asistan seni dinliyor..")
ses=dinleme()
print(ses)
