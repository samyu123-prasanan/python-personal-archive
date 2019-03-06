import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.reckontalk.com/cricket-players-date-of-birth/')
soup = BeautifulSoup(page.text, 'html.parser')    


div_tags = soup.select("div.panel panel-primary td")

print(div_tags)

for dts in div_tags:
    print(dts.text)


