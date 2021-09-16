# WORK IN PROGRESS ... ...

import requests
from bs4 import BeautifulSoup
import pprint
import lxml

response = requests.get("https://coinmarketcap.com/currencies/ethereum/")
soup = BeautifulSoup(response.text, "lxml")
price_class = soup.select(".priceValue")
divs = soup.find_all('div')

result = soup.find("div", {"class":".priceValue"})
print(result)
#print (result.text)
#print(divs)
print(price_class)
def real_price(divs):

    for item in (divs):
        
        anchors = item.find('text')
        #href_from_anchors = anchors.get("href")
        #title_from_anchors = anchors.get('title')
        print(anchors)
        
        
        


real_price(price_class)
