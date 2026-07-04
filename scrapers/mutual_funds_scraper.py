from bs4 import BeautifulSoup
import pandas as pd
import requests
url = "https://finance.yahoo.com/markets/mutualfunds/top/?guccounter=1"
headers = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; v64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_funds_data():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    soup.prettify()
    funds = soup.find_all("tr")
    Funds_data = []
# rows = soup.find_all("tr")
    for row in funds:
        cols= row.find_all("td")
        Funds_data.append([col.get_text(strip=True)for col in cols])

    return Funds_data
        