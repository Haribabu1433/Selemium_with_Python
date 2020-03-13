from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf,application/octet-stream") #Mime type for exe is application/octet-stream
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",r"C:\Users\hpolicha\Documents")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(executable_path=r"C:\Users\hpolicha\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe",
                                           firefox_profile=fp)
driver.get("https://www.google.com/chrome/")
driver.maximize_window()

driver.find_element_by_id("js-download-hero").click()
element = driver.find_element_by_id("js-accept-install")
element.click()
time.sleep(3)
#driver.switch_to_alert().accept()
#element.send_keys(Keys.ARROW_LEFT)
#element.send_keys(Keys.RETURN)