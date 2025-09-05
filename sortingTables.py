from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

# Click en el encabezado para ordenar por nombre
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Extraer todos los nombres de vegetales
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
web_sorted_veggies = [el.text for el in veggieWebElements]

# Crear una copia ordenada con Python
code_sorted_veggies = sorted(web_sorted_veggies, key=lambda x: x.lower())

# Comparar
assert web_sorted_veggies == code_sorted_veggies, (
    f"La tabla no está ordenada correctamente.\n"
    f"Esperado: {code_sorted_veggies}\n"
    f"Obtenido: {web_sorted_veggies}"
)

driver.quit()