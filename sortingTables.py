from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

sortedVeggies = []
#click on colum header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all veggies names -> veggieList (A,B,C)
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for element in veggieWebElements:
    sortedVeggies.append(element.text)

originalSortedList = sortedVeggies.copy()

# Sort this veggieList -> newSortedList
sortedVeggies.sort()

assert sortedVeggies == originalSortedList,"La tabla no está ordenada correctamente por nombre Veg/fruit name"