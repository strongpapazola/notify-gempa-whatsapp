# https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json
import requests
import urllib

def wa(payload):
    url = "http://103.41.206.252:8000/send-group-message"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def bmkg():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
    response = requests.request("GET", url)
    data = response.json()['Infogempa']['gempa']
    Tanggal = data["Tanggal"]
    Jam = data["Jam"]
    DateTime = data["DateTime"]
    Coordinates = data["Coordinates"]
    Lintang = data["Lintang"]
    Bujur = data["Bujur"]
    Magnitude = data["Magnitude"]
    Kedalaman = data["Kedalaman"]
    Wilayah = data["Wilayah"]
    Potensi = data["Potensi"]
    Dirasakan = data["Dirasakan"]
    Shakemap = data["Shakemap"]
    msg = f'Gempa Terkini\n\n{Tanggal}\n{Jam}\n\nSkala: {Magnitude} SR\n\n{Wilayah}\n\nhttp://www.google.com/maps/place/{Coordinates}'
    print(msg)
    return msg, Shakemap

from time import sleep

grup = [
    'Binance Smart Chain',
    'Rohen(dj)',
    'SICODING DEVELOPMENT',
]
temp = ""
while True:
    msg, shake = bmkg()
    if temp != msg:
        for i in grup:
            payload = {'name':i,'message':msg,'media':'true','url':f'https://data.bmkg.go.id/DataMKG/TEWS/{shake}'}
            urllib.parse.urlencode(payload)
            wa(payload)
        temp = msg
    print("sleeping...")
    sleep(5)