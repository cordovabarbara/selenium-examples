from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(3)
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

'''ActionChains es una clase de Selenium que simula acciones avanzadas del mouse y teclado que los usuarios hacen pero que click() normal no puede hacer.'''