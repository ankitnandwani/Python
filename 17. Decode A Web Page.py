import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.text)
for i in soup.find_all(class_="story-heading"):
    print(i)
