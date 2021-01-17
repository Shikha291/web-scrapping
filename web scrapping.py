import requests
import bs4
from bs4 import BeautifulSoup
res = requests.get('https://en.unesco.org/')
res.text
soup = BeautifulSoup(res.content,'html.parser')
links = soup.find_all(class_='region region-header-left')
print(links)
