import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_movies_data():
    driver = webdriver.Chrome()
    url = ("https://www.imdb.com/chart/top/")
    driver.get(url)
    time.sleep(5)
    movies = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")
    movies_data = []
    for movie in movies:
        title = movie.find_element(By.CSS_SELECTOR, "h4.ipc-title__text").text
        details = movie.find_elements(By.CSS_SELECTOR, "li.ipc-inline-list__item")
        year = details[0].text if len(details) > 0 else ""
        duration = details[1].text if len(details) > 1 else ""
        certificate = details[2].text if len(details) > 2 else ""
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text

        movies_data.append({
        "title": title,
        "year": year,
        "duration": duration,
        "certificate": certificate,
        "rating": rating
        })
    driver.quit()

    return movies_data