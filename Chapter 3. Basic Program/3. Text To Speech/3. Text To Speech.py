from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

en_text_path = 'enOndine.txt'
fr_text_path = 'frOndine.txt'
ko_text_path = 'koOndine.txt'

text_path = en_text_path
lang = 'en'

lang = input("Select lang (1. English | 2. French | 3. Korean): ")
if (lang == '1'):
    text_path = en_text_path
    lang = 'en'
elif (lang == '2'):
    text_path = fr_text_path
    lang = 'fr'
elif (lang == '3'):
    text_path = ko_text_path
    lang = 'ko'

with open(text_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang=lang)

tts.save("Ondine.mp3")

playsound("Ondine.mp3")