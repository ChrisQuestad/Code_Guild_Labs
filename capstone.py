import requests
from bs4 import BeautifulSoup
import csv
from lxml import html

# r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
# data = r.json()

# Get users Shopping List
shopping = input('Please enter your items: ')
# Append Items to empty list
shopping_list = []

for item in shopping:
    shopping_list.append(shopping.lower())
    break
print(shopping_list)

# Scrape data for users items
