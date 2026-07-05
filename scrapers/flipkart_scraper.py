


from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=shoes&as=on&as-show=on"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_flipkart_data():

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    shoes = soup.find_all("div", class_="nZIRY7")

    shoes_data = []

    for shoe in shoes:

        image = shoe.find("img")

        title = shoe.find("a", class_="atJtCj Qum9aC")

        price = shoe.find("div", class_="hZ3P6w")

        discount = shoe.find("div", class_="HQe8jr")

        size = shoe.find("div", class_="yZLfgx")

        shoes_data.append({

            "image": image["src"] if image else None,

            "title": title.get_text(strip=True) if title else "N/A",

            "price": price.get_text(strip=True) if price else "N/A",

            "discount": discount.get_text(strip=True) if discount else "N/A",

            "size": size.get_text(strip=True) if size else "N/A"

        })

    return shoes_data
