
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def scrape_books_data():
    driver = webdriver.Chrome()
    url = ("https://books.toscrape.com/")
    driver.get(url)
    time.sleep(3)
    books = driver.find_elements(By.CLASS_NAME, "col-xs-6.col-sm-4.col-md-3.col-lg-3")
    book_data = []
    for book in books:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")        
        price = book.find_element(By.CLASS_NAME, "price_color").text
        availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
    # title = book.find_element(By.CSS_SELECTOR, "a").get_attribute("title")   ## CSS_SELECTOR Iis used when somthing like <h3> inside 
        book_data.append({
        "title": title,
        "price": price,
        "availability": availability
        })
    driver.quit()
    return book_data