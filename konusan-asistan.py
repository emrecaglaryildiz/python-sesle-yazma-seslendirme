import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit = sr.Recognizer()
ses = ""


def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""
        try:
            ses = kayit.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan anlayamadı..")
        except sr.RequestError:
            print("Asistan çalışmıyor..")
        return ses


def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "a.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)


def yanıt(ses):
    if "köpük" in ses:
        print("seni duydum")
        if "merhaba" in ses:
            konusma("eyvallah sanada merhaba")
        if "nasılsın" in ses:
            konusma("hamdolsun çok iyiyim, sen nasılsın.")
        if "iyiyim" in ses:
            konusma("iyi olmana çok sevindim")
        if "fıkra" in ses:
            konusma(
                "Biliyorum, İlk defa helikopter gören Temel, Dursuna sormuş; Dursun, bu nedur da? Dursun, gayet sakin cevap vermiş;Haçan, bu olsa olsa bin yaşında bir sinek dur.")
        if "hikaye" in ses:
            konusma("hikaye mi, bizim hayatımız roman olmuş dostum")
        if "teşekkürler" in ses:
            konusma("çok kibarsın, ben teşekkür ederim")
        if "duyuyor musun" in ses:
            konusma("evet seni gayet iyi duyuyorum")
        if "sen kimsin" in ses:
            konusma("ben köpük sanal bir robotum sana yardım etmekten mutlu olurum, beni emre çağlar yıldız kodladı.")
        if "çıkış" in ses:
            konusma("çıkış yapılıyor")
            quit()
    else:
        konusma("seni anlayamadım, konuşurken adımı söylemelisin, benim adım köpük")


konusma("merhaba ben köpük")
print("Asistan çalışıyor..")

while True:
    ses = dinleme()
    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanıt(ses)
