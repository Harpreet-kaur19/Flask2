from bs4 import BeautifulSoup
import pandas as pd
import requests
url = "https://www.goodreads.com/quotes"
response = requests.get(url)
headers = {
    'user-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; v64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def scrape_quote_data():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    Quote = soup.find_all('div', class_ = 'quote')
    Quote_data = []
    for i in Quote:
        text = i.find("div", class_="quoteText").get_text(strip=True)
        author = i.find("span", class_="authorOrTitle").get_text(strip=True)
        likes = i.find("a", class_="smallText").get_text(strip=True)
        tags = i.find("div", class_="greyText smallText left").get_text(strip=True) if i.find("div", class_= "greyText") else None
    
        Quote_data.append({
        "text":text,
        "author": author,
        "likes": likes,
        "tags": tags
    })
    return Quote_data