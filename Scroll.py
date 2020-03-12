from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(10)

#1.Scroll down page by Pixels
#driver.execute_script("window.scrollBy(0,1500)","")

#2. Scroll down page till the element is visible
#element = driver.find_element(By.ID,"number")
#driver.execute_script("arguments[0].scrollIntoView();",element)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(10)
driver.close()