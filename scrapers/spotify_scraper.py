from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def scrape_spotify_data():

    driver = webdriver.Chrome()

    url = "https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg"

    driver.get(url)

    time.sleep(5)

    songs = driver.find_elements(
        By.CSS_SELECTOR,
        "div.GzWlvg0xI8IJiSoY.u5wEtE_x69YxkLdv"
    )

    song_data = []

    for song in songs:

        title = song.find_element(
            By.CSS_SELECTOR,
            "div.e-10451-text.encore-text-body-medium.encore-internal-color-text-base.lkqOvzjBxm0err2b.standalone-ellipsis-one-line"
        ).text

        artist = song.find_element(
            By.CSS_SELECTOR,
            "div.e-10451-text.encore-text-body-small a"
        ).text

        duration = song.find_element(
            By.CSS_SELECTOR,
            "div.e-10451-text.encore-text-body-small.encore-internal-color-text-subdued.Na06TEk5cCR4FwBd"
        ).text

        song_data.append({
            "title": title,
            "artist": artist,
            "duration": duration
        })

