from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

ddl = driver.find_element(By.ID,"searchDropdownBox")
drp = Select(ddl)
#select by visible text
drp.select_by_visible_text("Amazon Fashion")
time.sleep(3)
#select by index
drp.select_by_index(3)
#select by value
time.sleep(3)
drp.select_by_value("search-alias=alexa-skills")

#count number of options
print(len(drp.options))

# capture all the options and print
all_options = drp.options
for option in all_options:
    print(option.text)

time.sleep(5)
driver.close()
#driver.quit()


