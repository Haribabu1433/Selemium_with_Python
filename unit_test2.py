import unittest
from selenium import webdriver
import time
import logging

logging.basicConfig(filename=r"C:\Users\hpolicha\selenium\logging\Amazontest.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    )

logger = logging.getLogger()
logger.setLevel(logging.INFO) # by default logging level will be WARNING

#logging.debug("this is debug message")
#logging.info("this is info message")

def setUpModule():
    print("setUp module")
def tearDownModule():
    print("tearDownmodule")

class Amazon_search(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is login test")
    @classmethod
    def tearDown(self):
        print("this is logout")
    @classmethod
    def setUpClass(cls):
        print("open Application")
    @classmethod
    def tearDownClass(cls):
        print("close Application")
    def test_search_product(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\hpolicha\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.amazon.in")
        print(self.driver.title)
        logger.info("home page opened")
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys("lunch box")
        self.driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        logger.info("search of product done")
        print(self.driver.title)
        logger.info("waiting for 10sec for broweser to close")
        time.sleep(10)
        self.driver.close()




if __name__ == "__main__":
    unittest.main()