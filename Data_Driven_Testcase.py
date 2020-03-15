# this test case validates the usernames and passwords taken from excel and writed the result into the excel again
import XLUtils
import time
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    driver.maximize_window()
    driver.implicitly_wait(15)
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
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(
               EC.visibility_of_element_located((By.ID,"pageLoginAnchor"))
        )
        driver.execute_script("arguments[0].click()",element)

        #element.click()
        time.sleep(3)
        #driver.find_element(By.XPATH,"//span[contains(text(),'Log out')]").click()
        logout = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='js_15']/div/div/ul/li[14]/a"))
        )
        #logout = driver.find_element(By.XPATH,"//span[contains(text(), 'Log Out')]")
        #logout = driver.find_element(By.XPATH,"//*[@id='js_d']/div/div/ul/li[14]/a")
        driver.execute_script("arguments[0].click()", logout)



