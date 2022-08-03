import gtts
import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
from os import path

dosya = open("test.txt", encoding="utf-8")
metin = dosya.read()
cikti = gTTS(text=metin, lang='tr')
ses = "test1.mp3"
cikti.save(ses)
playsound(ses)
dosya.close()



