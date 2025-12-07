from hmac import new
from bs4 import BeautifulSoup
import requests
import urllib3 
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://scrapeme.live/shop/"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')


## Getting Products Names 
product_name = soup.find_all( "h2", class_ = "woocommerce-loop-product__title")

## Getting Products Prices
product_price= soup.find_all("span", class_="woocommerce-Price-amount amount")

## Saving Data to csv file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file : 
    writer= csv.writer(file)
    writer.writerow(['Product Name','Price'])

    for product, price in zip (product_name, product_price):
        name_text= product.text
        price_text= price.text 
        writer.writerow([name_text, price_text])


        print(f"Saved: {name_text} - {price_text}")