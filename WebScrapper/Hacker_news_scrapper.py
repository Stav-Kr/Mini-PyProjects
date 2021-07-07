# Simple web scrapper that prints in order from lowest to highest the articles 
# from the first 3 pages of the website Hacker News, that have more than 100 points each 
# (Based on ZTM Python Developer course)
# Order of articles can be changes by setting the reverse=True on line 29
import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news?/p=i/")
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select(".storylink")
subtext = soup.select(".subtext")

for i in range(1, 4):

    def hacker_news_custom(links, subtext):
        hn = []
        for inx, item in enumerate(links):
            title = links[inx].getText()
            url = links[inx].get("href", None)
            vote = subtext[inx].select(".score")
            if len(vote):
                point_votes = int(vote[0].getText().replace("points", ""))
                if point_votes > 99:
                    hn.append({"title": title, "link": url, "votes": point_votes})
        return sorted_articles(hn)

    def sorted_articles(hnlist):
        return sorted(hnlist, key=lambda k: k["votes"], reverse=False)

    print("-"*10, "page ", i, "-"*10)
    pprint.pprint(hacker_news_custom(links, subtext))
