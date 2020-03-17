import unittest

class ApplicationTest(unittest.TestCase):
    @unittest.SkipTest # decorator to skip the test case
    def test_search(self):
        print("this is search test case")
    @unittest.skip("i am skipped bacause told to skip") # skip with reason
    def test_advancedsearch(self):
        print("this is adv search")
    @unittest.skipIf(5==5,"numbers are equal")
    def test_prepaidrecharge(self):
        print("this is prepaid recharge")
    def test_postpaidreacharge(self):
        print("this is postpaid recharge")
    def test_logout(self):
        print("logging out")

if __name__ == "__main__":
    unittest.main()