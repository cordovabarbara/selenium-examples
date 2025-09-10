from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

def addProductToCart(productToAdd, products):
    for product in products:
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == productToAdd:
            product.find_element(By.XPATH, "div/button").click()
            break

# Usar la función
addProductToCart("Samsung Note 8", products)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("spa")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Spain")))
driver.find_element(By.LINK_TEXT,"Spain").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
alertsuccess = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in alertsuccess

driver.close()