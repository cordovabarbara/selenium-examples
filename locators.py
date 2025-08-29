import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath  //tagname[@attribute='value']
# CSS   //input[@type='submit'] #id, .class
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Barbara")

#static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.NAME, "bday").send_keys("1995-01-01")
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello again")
time.sleep(4)

