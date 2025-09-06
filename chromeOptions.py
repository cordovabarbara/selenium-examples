from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

options = Options()
options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)

driver.quit()