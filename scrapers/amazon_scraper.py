from bs4 import BeautifulSoup
import pandas as pd
import requests

url = ("https://www.amazon.in/s?k=laptop&crid=YLH7SZQM1WE6&sprefix=laptop%2Caps%2C610&ref=nb_sb_noss_2")
response = requests.get(url)
headers = {
    'user-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; v64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrap_amazon_data():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    soup.prettify()

    Amazon = soup.find_all("div", class_="puis-card-container puis-overflow-hidden s-card-container aok-relative desktop-list-view puis-include-content-margin puis puis-v2lstc5p0oad1j2pqjic4rhsbvr s-latency-cf-section puis-card-border")

    Amazon_data=[]

    for product in Amazon:
        title = product.find("h2", class_="a-size-medium")
        price = product.find("span", class_="a-price-whole")
        mrp = product.find("span", class_="a-text-price")
        discount = product.find("span", class_="a-letter-space")
        rating = product.find("span", class_="a-icon-alt")
        reviews = product.find("span", class_="a-size-base")
        image = product.find("img", class_="s-image")
    
        Amazon_data.append({
        "image": image["src"] if image else None,
        "title": title.text.strip() if title else "N/A",
        "price": price.text.strip() if price else "N/A",
        "mrp": mrp.text.strip() if mrp else "N/A",
        "discount": discount.text.strip() if discount else "N/A",
        "rating": rating.text.strip() if rating else "N/A",
        "reviews": reviews.text.strip() if reviews else "N/A"
        })

    return Amazon_data

