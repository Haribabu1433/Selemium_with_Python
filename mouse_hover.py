from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

email = "policharlaharibabu01@gmail.com"
password = "haribabu1433"
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
account = driver.find_element_by_id("nav-link-accountList")
sign_in = driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a")

actions = ActionChains(driver)
actions.move_to_element(account).move_to_element(sign_in).click().perform()

driver.find_element_by_id("ap_email").send_keys(email)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(password)
driver.find_element_by_id("signInSubmit").click()

assert "Online Shopping" in driver.title
print("login successful")





