import requests
from bs4 import BeautifulSoup

req = requests.get('http://github.com')
data = req.text

soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):
    print link['href']
