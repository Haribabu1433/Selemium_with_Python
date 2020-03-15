from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in")

cookies = driver.get_cookies()

print(len(cookies),"\n",cookies)

driver.add_cookie({'name':"Cookie1","value":"234"})
cookies = driver.get_cookies()
print(len(cookies),"\n",cookies)

driver.delete_cookie("Cookie1")
cookies = driver.get_cookies()
print(len(cookies),"\n",cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies),"\n",cookies)

