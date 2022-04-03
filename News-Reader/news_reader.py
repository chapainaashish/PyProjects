# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# getting news from api and listening it

import requests
import os
from gtts import gTTS
from datetime import date
from datetime import datetime

news_api = requests.get(
    "https://newsapi.org/v2/top-headlines?country=us&apiKey=dd40b7f73d424f11b50a5212d54908b4")

actual_news = news_api.json()["articles"]

news_text = f"""Hello, I am Emma Harris reporting from Capital Hall U.S., Welcome to Syncfield News, 
Today is {date.today().strftime("%B %d, %Y")} and the current time in Washington is {datetime.now().strftime("%H:%M")}
So, let's begin our news boletin
"""

for news in actual_news:
    try:
        news_text = "" + news_text + news['title'] + "."
        news_text = news_text + news['description'] + "\n\nNext news\n"
    except:
        pass

news_text = news_text.rstrip("\n\nNext news\n")

news_text = news_text + "Thank you, Have a good day."

print("Fetching data from server...")

language = "en"


speech = gTTS(text=news_text, lang=language)
speech.save(
    "/home/aashishsharma/Documents/python_journey/dependencies_files/news.mp3")

os.system(
    "mpg321 /home/aashishsharma/Documents/python_journey/dependencies_files/news.mp3")
