from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

links = driver.find_elements(By.TAG_NAME,"a") # grabs all the links on this page

print("number of links in page:",len(links)) # count of links present

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,"Today's Deals").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Toda").click()

time.sleep(5)
driver.close()
