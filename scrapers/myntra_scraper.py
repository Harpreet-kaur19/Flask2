import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_myntra_data():
    driver = webdriver.Chrome()

    url = "https://www.myntra.com/men-tshirts"
    driver.get(url)

    time.sleep(5)


    products = driver.find_elements(By.CSS_SELECTOR, "li.product-base")

    myntra_data = []
    # for product in products:

    #     brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
    #     name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text
    #     price = product.find_element(By.CSS_SELECTOR, "span.product-discountedPrice").text
    #     original_price = product.find_element(By.CSS_SELECTOR, "span.product-strike").text
    #     discount = product.find_element(By.CSS_SELECTOR, "span.product-discountPercentage").text
        
    #     myntra_data.append({
    #     "Brand": brand,
    #     "Product": name,
    #     "Price":price,
    #     "Original Price": original_price,
    #     "Discount": discount
    #     })
    
    for product in products:

        brand = product.find_element(By.CSS_SELECTOR, "h3.product-brand").text
        name = product.find_element(By.CSS_SELECTOR, "h4.product-product").text

    # Price
        discounted = product.find_elements(By.CSS_SELECTOR, "span.product-discountedPrice")
        normal = product.find_elements(By.CSS_SELECTOR, "span.product-price")

        if discounted:
            price = discounted[0].text
        elif normal:
            price = normal[0].text
        else:
             price = "N/A"

    # Original Price
        strike = product.find_elements(By.CSS_SELECTOR, "span.product-strike")
        if strike:
            original_price = strike[0].text
        else:
            original_price = "-"

    # Discount
        discount_ele = product.find_elements(By.CSS_SELECTOR, "span.product-discountPercentage")
        if discount_ele:
             discount = discount_ele[0].text
        else:
             discount = "-"

        myntra_data.append({
        "Brand": brand,
        "Product": name,
        "Price": price,
        "Original Price": original_price,
        "Discount": discount
        })
    driver.quit()
    return myntra_data