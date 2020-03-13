from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": r"C:\Users\hpolicha\Documents"}) # to customize the downloads directory

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe",options=chromeOptions)
driver.get("https://www.google.com/chrome/")
driver.maximize_window()

driver.find_element_by_id("js-download-hero").click()
driver.find_element_by_id("js-accept-install").click()
