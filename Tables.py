from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.implicitly_wait(10) # this 10sec applies all to all the elements

rows = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))

print(rows,cols)
for col in range(1,cols+1):
    print(driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th["+str(col)+"]").text, end='    ')
print()

for row in range(2,rows+1):
    for col in range(1,cols+1):
        print(driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(row)+"]/td["+str(col)+"]").text,end= '    ')
    print()

time.sleep(5)
driver.close()





