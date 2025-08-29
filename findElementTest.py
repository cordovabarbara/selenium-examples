import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("can")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li.ui-menu-item a") #lista de sugerencias
print(len(countries))

for country in countries:
    if country.text.strip().lower() == "canada":
        country.click()
        break

value = driver.find_element(By.ID, "autosuggest").get_attribute("value")
#original assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Canada"
# Normalizamos: quitamos espacios y pasamos a minúsculas
assert value.strip().lower() == "canada"
#El assert es el check automático que valida que tu acción funcionó.

time.sleep(3)

driver.quit()