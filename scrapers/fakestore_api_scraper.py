import requests
import pandas as pd

def scrape_fakestore_api_data():
    url = ("https://fakestoreapi.com/products")
    response = requests.get(url)
    data = response.json()
    return data