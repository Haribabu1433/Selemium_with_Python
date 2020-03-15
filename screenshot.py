from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in")

#driver.save_screenshot(r"C:\Users\hpolicha\selenium\homepage.png") # format can be jpg as well

driver.get_screenshot_as_file(r"C:\Users\hpolicha\selenium\homepage2.png")