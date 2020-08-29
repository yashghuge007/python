from gtts import gTTS

import os

f = open('Sample.txt')

x = f.read()

language = 'en'

audio = gTTS(text=x,lang=language,slow=False)

audio.save("Sa.wav")

os.system("Sa.wav")

