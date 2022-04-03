# Author: Aashish Sharma
# Github: https://github.com/aasis2520c
# NOTE here we are using gtts because it can convert text into speech clearly
from gtts import gTTS
import os
text = """
to defeat a thief, you have to think like a thief.
"""

language = "en"


speech = gTTS(text=text, lang=language, slow=False)
speech.save(
    "/home/aashish/Documents/python_journey/dependencies_files/text_speech.mp3")

# mpg321 is a external command of linux to play mp3 file in terminal
os.system(
    "mpg321 /home/aashish/Documents/python_journey/dependencies_files/text_speech.mp3")
