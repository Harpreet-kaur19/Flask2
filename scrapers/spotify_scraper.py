# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# def scrape_spotify_data():

#     driver = webdriver.Chrome()

#     url = "https://open.spotify.com/playlist/37i9dQZEVXbLZ52XmnySJg"

#     driver.get(url)

#     time.sleep(5)

#     songs = driver.find_elements(
#         By.CSS_SELECTOR,
#         "div.GzWlvg0xI8IJiSoY.u5wEtE_x69YxkLdv"
#     )

#     song_data = []

#     for song in songs:

#         title = song.find_element(
#             By.CSS_SELECTOR,
#             "div.e-10451-text.encore-text-body-medium.encore-internal-color-text-base.lkqOvzjBxm0err2b.standalone-ellipsis-one-line"
#         ).text

#         artist = song.find_element(
#             By.CSS_SELECTOR,
#             "div.e-10451-text.encore-text-body-small a"
#         ).text

#         duration = song.find_element(
#             By.CSS_SELECTOR,
#             "div.e-10451-text.encore-text-body-small.encore-internal-color-text-subdued.Na06TEk5cCR4FwBd"
#         ).text

#         song_data.append({
#             "title": title,
#             "artist": artist,
#             "duration": duration
#         })

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_spotify_data():

    options = webdriver.ChromeOptions()

    # Required for Render/Linux
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

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

    driver.quit()

    return song_data

    driver.quit()

    return song_data
