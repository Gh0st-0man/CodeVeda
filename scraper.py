from bs4 import BeautifulSoup
import requests
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://scrapeme.live/shop/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


## Getting Products Names 
product_name = soup.find_all( "h2", class_ = "woocommerce-loop-product__title")

for product in product_name:
    print(product.text)

## Getting Products Prices
product_price= soup.find_all("span", class_="woocommerce-Price-amount amount")
for price in product_price:
    print(price.text)

for product, price in zip(product_name, product_price):
    print(f"{product.text} - {price.text}")

 