from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
source_ele = driver.find_element_by_id("draggable")
dest_ele = driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source_ele,dest_ele).perform()

time.sleep(10)
driver.close()