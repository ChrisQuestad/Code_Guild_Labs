import requests
from bs4 import BeautifulSoup

# Get users Shopping List
shopping = input('Please enter your items: ')

# Append Items to empty list
shopping_list = []

for item in shopping:
    shopping_list.append(shopping.lower())
    break
print(shopping_list)

# Scrape data for users items
if __name__ == '__main__':
    response = requests.get('http://www.SupermarketAPI.com/api.asmx/COMMERCIAL_SearchByProductName?APIKEY=APIKEY&ItemName=Parsley')
    response.raise_for_status()
    html = BeautifulSoup(response.text, 'html.parser')
    print(html)
