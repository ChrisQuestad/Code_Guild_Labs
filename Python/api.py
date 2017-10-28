import requests

from bs4 import BeautifulSoup


if __name__ == '__main__':
    response = requests.get('http://www.SupermarketAPI.com/api.asmx/COMMERCIAL_SearchByProductName?APIKEY=APIKEY&ItemName=Parsley')
    response.raise_for_status()
    html = BeautifulSoup(response.text, 'html.parser')
    print(html)
