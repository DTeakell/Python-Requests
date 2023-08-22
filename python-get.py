# Date: 7/27/2023
# File: Calculator.py
# Name: Dillon Teakell
# Desc: Calculator using Python 
#
#

import requests

def main():

    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    data = response.json()
    print(data)


main()