from gtts import gTTS


def tts(text):
    textToMP3 = gTTS(text=text, lang='ko')
    textToMP3.save("translate.mp3")
