import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "checkBoxOption2").click()
'''
Ejemplo del profesor
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print (len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
    checkbox.click()
    assert checkbox.is_selected()
    break
'''
#Los radio buttons son excluyentes: solo se puede seleccionar uno a la vez.
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# 1. Verifica que el input con id="displayed-text" está visible en pantalla
assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(1)

# 2. Hace click en el botón con id="hide-textbox"
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(1)

# 3. Verifica que ahora ese input ya no está visible
assert not driver.find_element(By.ID, "displayed-text").is_displayed()



time.sleep(3)

driver.quit()

