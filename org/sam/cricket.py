import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.espncricinfo.com/india/content/player/30045.html')
soup = BeautifulSoup(page.text, 'html.parser')    

def is_month(content):
    content = content.lower()
    if ('july' in content):
        return True
    if ('june' in content):
        return True
    return False 

div_tags = soup.select("div p.ciPlayerinformationtxt")

#print(div_tags)

for dts in div_tags:
    if (is_month(dts.text)):
        print(dts.text)


