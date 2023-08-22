# Date: 7/27/2023
# File: Calculator.py
# Name: Dillon Teakell
# Desc: Calculator using Python 
#
#

import requests

def get_data(url):
    response = requests.get(url)
    response.json()
    print(response)


def main():

    get_data(url="https://jsonplaceholder.typicode.com/todos/1")


main()