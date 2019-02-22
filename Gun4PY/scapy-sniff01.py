#! /usr/bin/env python3
 
import json
import requests
from collections import Counter
from scapy.all import sniff
 
# API opsiyonlarini tanimla
url = "http://hosted.app/api/packets"
token = "supersecretusertoken"
 
def custom_action(url: str, token: str):
 
  def upload_packet(packet):
    # verilen parametrelerle paketi yukle 
    headers = {'content-type': 'application/json'}
    data = {
        'paket': packet.summary(),
        'token': token,
    }
    r = requests.post(url, data=data, headers=headers)
 
  return upload_packet
 
sniff(prn=custom_action(url, token))
