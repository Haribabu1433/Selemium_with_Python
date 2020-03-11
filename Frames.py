from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # First frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") # second frame
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]").click()

time.sleep(5)
driver.close()
