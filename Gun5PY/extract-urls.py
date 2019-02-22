#
# Gerekli modulleri import ediyoruz	
from bs4 import BeautifulSoup
import requests

# İlk olarak web sitesinin adresini istiyoruz
url = raw_input("Web sitesini girin: ")
# Daha sonra requests modulu ile bu siteyi alıyoruz
req  = requests.get("http://" +url)

# Alınan bu siteyi aöık metin haline getirmek icin
# requests modulunun text fonksiyonunu kullaniyoruz
data = req.text

# BeautifulSoup nesnesi olusturuyoruz
# Ve bu nesneyi web sitesinin açık metni ile dolduruyoruz
soup = BeautifulSoup(data)

# find_all fonksiyonu bütün a tag'lerini
# uzerinden gecerek, href feature'nin degerini
# alıp ekrana yazdırıyoruz.
for link in soup.find_all('a'):
   print link.get('href')
