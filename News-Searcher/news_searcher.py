# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

"""Advance News Searcher"""
from datetime import date
import requests


class Searcher:
    """An advance news searcher class"""

    def __init__(self, query):
        self.query = query
        self.apikey = "your api key"

    def list_unpacker(self, input_list):
        """Unpack the list and print in the terminal"""
        print("\nRelated News;")
        for item in input_list:
            print(f"{item}\n")

    def articles(self, raw_list):
        """To parse articles according to their description"""
        try:
            news_articles = raw_list.json()["articles"]
        except KeyError:
            print("Upgrade your plan in NEWSAPI to unlock this content!")
            exit()
        searched_news = []
        for news in news_articles:
            searched_news.append(news['description'])
        return searched_news

    def manual_search(self, combined_date):
        """Seaching news in manual date"""
        url = f"https://newsapi.org/v2/everything?q={self.query}&from={combined_date}&sortBy=popularity&apiKey={self.apikey}"
        url_news = requests.get(url)
        news_list = self.articles(url_news)
        self.list_unpacker(news_list)

    def auto_search(self):
        """Searching news in current date"""
        url = f"https://newsapi.org/v2/everything?q={self.query}&from={date.today()}&sortBy=popularity&apiKey={self.apikey}"
        news_api = requests.get(url)
        news_list = self.articles(news_api)
        self.list_unpacker(news_list)


if __name__ == '__main__':
    query = str(input("\nEnter your search query: "))
    news = Searcher(query)
    search_type = str(input("Press 'd' to search by date [d/*] "))

    if search_type == "d":
        print(
            "\nAttention: To search the news before one month, Upgrade your Plan in NEWSAPI")
        search_year = str(input("Enter the year: ")).strip()
        search_month = str(input("Enter the month: ")).strip()
        search_day = str(input("Enter the day: ")).strip()

        combined_date = f"{search_year}-{search_month}-{search_day}"
        news.manual_search(combined_date)

    else:
        news.auto_search()
