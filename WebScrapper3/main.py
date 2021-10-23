# WORK IN PROGRESS ... ...

import requests
from bs4 import BeautifulSoup
import pprint
import re
import lxml

response = requests.get("https://ethereumprice.org/live/")
soup = BeautifulSoup(response.text, "lxml")
get_price = soup.find_all( 'td')
print(get_price)
#price_class = get_price.find(".subPrice")
# soup1 = BeautifulSoup("""<div id="coin-price" class="headline flash" >
#  <span class="currency-symbol">$</span>
#  <span class="value">5</span> </div>""", "xml")
#print(soup)
#print(price_class)
# print(soup1.select_one("span[class*=value]").text)

#print(price_class[:1])


