import requests
import pandas as pd
def scrape_json_data():

    url = ("https://jsonplaceholder.typicode.com/posts")
    response = requests.get(url)
    posts = response.json()

    return posts