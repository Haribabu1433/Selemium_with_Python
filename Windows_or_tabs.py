from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.timespoints.com/earn")

element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div[1]/div[2]/div[2]/div[2]/div/a[7]/div[1]/div/div[1]"))
            )
element.click()

handles = driver.window_handles
print(driver.current_window_handle)

for handle in handles:
    driver.switch_to.window(handle)
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/div/figure/a"))
    )
element.click()

time.sleep(5)
#driver.quit()