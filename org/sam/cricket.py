import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Ajinkya_Rahane')
soup = BeautifulSoup(page.text, 'html.parser')    

div_tags = soup.select("div.mw-parser-output p")

print(div_tags)

for dts in div_tags:
    print(dts.text)


