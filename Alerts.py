from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")


element = driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button")
element.click()

driver.switch_to_alert().accept()
time.sleep(5)
element.click()
driver.switch_to_alert().dismiss()



time.sleep(10)
driver.close()