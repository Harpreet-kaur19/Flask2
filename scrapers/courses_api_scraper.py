import requests
import pandas as pd

def scrape_courses_data():
    url = ("https://gyansetu.codroidhub.com/api/courses?view=user")
    response = requests.get(url)
    data = response.json()
    return data