from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")

check_box = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/input[2]")
if(not check_box.is_selected()):
    check_box.click()
print(check_box.is_selected())

radio_button = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/input[4]")
radio_button.click()
print(radio_button.is_selected())

driver.close()