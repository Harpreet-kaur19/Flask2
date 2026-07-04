import requests
import pandas as pd

def scrape_dummy_json_data():
    url = ("https://dummyjson.com/products")
    response = requests.get(url)
    data = response.json()
    return data