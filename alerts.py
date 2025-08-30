import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Barbara"

#probar selectores CSS
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
time.sleep(3)
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss() para seleccionar cancelar
