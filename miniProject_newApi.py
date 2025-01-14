#(type(response.text))
#print(response.text)
import requests
import json
x=input("enter the type of news you want to hear ")
url=f'https://newsapi.org/v2/everything?q={x}&from=2024-11-23&to=2024-11-23&sortBy=popularity&apiKey=657a9316411e464f857869db68565a2d'
response=requests.get(url)
news=json.loads(response.text)
for article in news['articles']:
    print('Title :',article['title'])
    print(article['description'])
    print('-----------------------------------------------------------------')