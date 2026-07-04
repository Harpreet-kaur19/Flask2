from bs4 import BeautifulSoup
import pandas as pd
import requests
url = "https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=137bfca7-eb1c-4aa8-8ce9-79a525bf0eb2"
response = requests.get(url)
headers ={
    'user-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; v64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_flipkart_data():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup.prettify()
    shoes = soup.find_all('div', class_= 'nZIRY7')
    shoes_data  = []
    for i in shoes:
    
        title = i.find("a", class_="atJtCj Qum9aC")     
        price = i.find("div", class_="hZ3P6w")         
        discount = i.find("div", class_= "HQe8jr")      
        size = i.find("div", class_= "yZLfgx")        

        shoes_data.append({
        "title":title,
        "price":price,
        "discount" : discount,
        "size":size
    })

    return shoes_data