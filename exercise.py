import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()


driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("brbacordova@gmail.com")
# yo pude identicar asi driver.find_element(By.ID, "userPassword").send_keys("Maracaibo123+")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Maracaibo123+")
driver.find_element(By.ID, "confirmPassword").send_keys("Maracaibo123+")
# con cc_selector si no hay id driver.find_element(By.CSS_SELECTOR, "input#confirmPassword").send_keys("Maracaibo123+")
# driver.find_element(By.XPATH, "//button[type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


time.sleep(4)

driver.quit()