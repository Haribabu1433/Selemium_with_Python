# this test case validates the usernames and passwords taken from excel and writed the result into the excel again

import XLUtils
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

path = r"C:\Users\hpolicha\Documents\pyexcel\data1.xlsx"
sheet = "Validation"
rows = XLUtils.getRowCount(path,sheet)
driver_path = r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe"
webpage = "https://www.facebook.com/"
driver = webdriver.Chrome(executable_path=driver_path)

for r in range(2,rows+1):
    username = XLUtils.readData(path,sheet,r,1)
    password = XLUtils.readData(path,sheet,r,2)
    driver.get(webpage)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_id("email").send_keys(username)
    element = driver.find_element_by_id("pass")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    if(driver.title == "Log in to Facebook | Facebook"):
        print("testfailed")
        XLUtils.WriteData(path,sheet,r,3,"failed")
    else:
        print("testpassed")
        XLUtils.WriteData(path, sheet, r, 3, "passed")

        driver.find_element_by_id("pageLoginAnchor").click()
        #driver.find_element(By.XPATH,"//span[contains(text(),'Log out')]").click()
        driver.find_element_by_xpath("/html/body/div[19]/div/div/div/div/div[1]/div/div/ul/li[14]/a/span/span").click()



