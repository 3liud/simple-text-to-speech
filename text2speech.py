from gtts import gTTS
import os

# selectign the language to be used 
language = 'en'

# simple text string to be converted/ read.
text2read = "here is a simple text to speech conversion using google text to speech library. It requires the internet!"

# creating the speech object
speech = gTTS(text = text2read, lang= language, slow= False)

# save the converted text into a voice file
speech.save("readText.mp3")

# playign the audio file using linux play command usign sox

os.system("play readText.mp3")


