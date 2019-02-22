import requests
from bs4 import BeautifulSoup

def scrape(url):
   headers = requests.utils.default_headers()
   headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20190101 Firefox/52.0',})
   req = requests.get(url, headers)
   raw_html = req.content
   soup = BeautifulSoup(raw_html, 'html.parser')
   
   print(soup.prettify())

url = raw_input("Web sitesini giriniz: ")
scrape('http://' + url)
