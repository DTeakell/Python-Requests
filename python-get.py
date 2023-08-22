# Date: 7/27/2023
# File: Calculator.py
# Name: Dillon Teakell
# Desc: Calculator using Python 
#
#

import requests

def get_api(url):

    response = requests.get(url)
    data = response.json()
    print(data)


def main():

    latitude = 37.3541
    longitude = -121.9552

    url = f"https://api.open-meteo.com/v1/gfs?latitude={latitude}&longitude={longitude}&current_weather"\
    f"?latitude={latitude}"\
    f"?longitude={longitude}"\
    
    get_api(url)

main()