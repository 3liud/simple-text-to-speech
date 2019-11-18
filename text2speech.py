from gtts import gTTS
import os

# selectign the language to be used 
language = 'en'

# enter the text you want to be covnert here
print("enter your text here!")
text2convert = input(" ")

# simple text string to be converted/ read.
text2read = text2convert
'''
#text2read = """
	My dreams haven’t gone that far.
	I think I should wake up now. 
    
    by Eliud.
"""
'''

# creating the speech object
speech = gTTS(text = text2read, lang= language, slow= False)

# save the converted text into a voice file
speech.save("readText.mp3")

# playign the audio file using linux play command usign sox

os.system("play readText.mp3")


