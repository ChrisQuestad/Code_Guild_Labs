import requests
from bs4 import BeautifulSoup
shopping = input('Please enter your items: ')
shopping_list = []

for item in shopping:
    shopping_list.append(shopping.lower())
    break
print(shopping_list)


shopping_list = soup.find(class_='BodyText')


for item in shopping_list:
    shopping_list_items = shopping_list.find_all(item)
    print(shopping_list_items)
