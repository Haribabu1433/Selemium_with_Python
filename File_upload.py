from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
driver.maximize_window()

#driver.switch_to.frame(0) # form or frame based on index value

driver.find_element_by_id("myFile").send_keys("C://Users/hpolicha/Pictures/profile_pic.jpg")

#driver.find_element_by_id("submit").click()