import requests
import pandas as pd

def scrape_feedbacks_data():
    url = ("https://gyansetu.codroidhub.com/api/feedbacks")
    response = requests.get(url)
    data = response.json()
    return data