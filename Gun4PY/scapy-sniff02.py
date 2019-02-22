import json
import requests
from collections import Counter
from functools import partial
from scapy.all import sniff
 
# API opsiyonlarini tanimla
url = "http://hosted.app/api/packets"
token = "supersecretusertoken"
 
 
def upload_packet(api_endpoint: str, api_token: str, packet):
    # verilen parametrelerle paketi yukle
    headers = {'content-type': 'application/json'}
    data = {
        'packet': packet.summary(),
        'token': api_token,
    }
    r = requests.post(api_endpoint, data=data, headers=headers)
 
sniff(prn=partial(upload_packet, url, token))
