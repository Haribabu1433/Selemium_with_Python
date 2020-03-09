from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path=r"C:\Users\hpolicha\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe")

driver.get("https://www.google.com")

print(driver.title)
#print(driver.current_url)

element = driver.find_element_by_link_text("Images")
print(element.is_displayed())
print(element.is_enabled())
print(element.is_selected())

driver.quit()