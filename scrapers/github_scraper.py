import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_github_data():

    driver = webdriver.Chrome()

    driver.get("https://github.com/trending")

    time.sleep(5)

    repositories = driver.find_elements(By.CSS_SELECTOR, "article.Box-row")

    github_data = []

    for repo in repositories:

        github_data.append({

            "Repository": repo.find_element(By.CSS_SELECTOR, "h2 a").text.replace("\n", ""),

            "Description": repo.find_element(By.CSS_SELECTOR, "p").text,

            "Language": repo.find_element(By.CSS_SELECTOR, "span[itemprop='programmingLanguage']").text,

            "Stars": repo.find_element(By.CSS_SELECTOR, "a[href$='/stargazers']").text,

            "Forks": repo.find_element(By.CSS_SELECTOR, "a[href$='/forks']").text,

            "Image": repo.find_element(By.CSS_SELECTOR, "img.avatar").get_attribute("src")

        })

    driver.quit()

    return github_data