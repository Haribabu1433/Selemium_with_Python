from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=r"C:\Users\hpolicha\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")


driver.get("https://www.google.com")

driver.maximize_window()
driver.implicitly_wait(5)

assert "Google" == driver.title
print(driver.title)
#print(driver.current_url)

## Explicit wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Images")))

element.click()

driver.quit()