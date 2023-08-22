# Date: 8/21/2023
# File: python-get.py
# Name: Dillon Teakell
# Desc: GET Method using Requests
#
#

import requests

# GET
def get_api(url):

    response = requests.get(url)
    data = response.json()
    print(data)


def main():

    # Set custom parameters for getting custom results
    latitude = 37.3541
    longitude = -121.9552

    # Use f-statements to format URL to use custom parameters
    url = f"https://api.open-meteo.com/v1/gfs?latitude={latitude}&longitude={longitude}&current_weather"

    #Call function
    get_api(url)

main()