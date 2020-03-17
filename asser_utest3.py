import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
        self.assertIsNotNone(driver) # true if driver is not None
        #self.assertIsNone(driver) # true if driver is None
        driver.get("https://www.google.com")
        print(driver.title)


if __name__ == "__main__":
    unittest.main()