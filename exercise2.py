import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(7)

#Click en el link
driver.find_element(By.PARTIAL_LINK_TEXT, "Free Access").click()

#Guardar los handles
windowsOpened = driver.window_handles

#Cambiar a la nueva ventana
driver.switch_to.window(windowsOpened[1])
time.sleep(6)

#Obtener el correo en la nueva ventana
email = driver.find_element(By.CSS_SELECTOR,"p.im-para.red a").text
print("Correo encontrado:", email)

#Cerrar Ventana
driver.close()
driver.switch_to.window(windowsOpened[0])


#pegar texto en el input
driver.find_element(By.ID, "username").send_keys(email)

#poner password
driver.find_element(By.ID, "password").send_keys("123456789")

#Marcar boton
driver.find_element(By.ID, "usertype"). click()

#dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select.form-control"))
dropdown.select_by_visible_text("Student")

#Sign in
driver.find_element(By.ID, "signInBtn").click()

#message
error_message = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger"))
).text

print("Mensaje de error:", error_message)

# cerrar el navegador
driver.quit()


