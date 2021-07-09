# scrapes https://metro.co.uk/news/ for discounds displayed on the page

import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://metro.co.uk/news/")
soup = BeautifulSoup(response.text, "html.parser")
discount_class = soup.select(".metro-discount-codes clearfix")
links = soup.select(".metro-discount-codes-item")
a_disc = soup.find_all(target="_blank")


def discounds(links):

    for item in (links):
        
        anchors = item.find("a")
        href_from_anchors = anchors.get("href")
        pprint.pprint(href_from_anchors)
        # title = links[index].getText()
        pprint.pprint(href_from_anchors)


discounds(links)
