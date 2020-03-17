import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
        list1 = ["python","java","selenium"]
        #self.assertIn("python",list1)
        self.assertNotIn("ruby",list1)
        driver.get("https://www.google.com")
        print(driver.title)


if __name__ == "__main__":
    unittest.main()