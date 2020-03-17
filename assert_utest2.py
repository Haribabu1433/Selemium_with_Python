import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com")
        pagetitle = driver.title
        #self.assertTrue("Google"==pagetitle) # pass when both are equal
        self.assertFalse("Google123"==pagetitle)# pass when both are different or unequal


if __name__ == "__main__":
    unittest.main()