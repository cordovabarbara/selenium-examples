from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.switch_to.frame("courses-iframe")
driver.find_element(By.CSS_SELECTOR, "a[href*='courses']").click()
driver.switch_to.default_content()
driver.find_element(By.ID, "checkBoxOption1").click()
time.sleep(2)
driver.quit()
