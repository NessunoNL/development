from bs4 import BeautifulSoup
import requests

searchtext = "Wusthof ikon classic 20cm"
source = requests.get(f'https://www.bol.com/nl/s/?searchtext={searchtext}').text

soup = BeautifulSoup(source, 'lxml')

for product in soup.find_all('li', class_="product-item--row js_item_root"):

    product_title = product.find('div', class_="product-title--inline").find('a').text
    img_url = product.find('div', class_="h-o-hidden").a.img['src']
    product_url = "https://www.bol.com" + product.find('div', class_="product-title--inline").find('a')['href']
    price = product.find('span', class_="promo-price").text.split("\n")
    price_total = int(price[0]) + (int(price[1]) / 100)

    print(product_title)
    print(product_url)
    print(img_url)
    print(str(price_total) + " euro")
    print()
    print("---------------------------------------------")
    print()
