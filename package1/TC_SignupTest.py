import unittest

class Signuptest(unittest.TestCase):
    def test_signupbyemail(self):
        print("this is sighn by email test")
        self.assertTrue(True)
    def test_signupbyFacebook(self):
        print("this is sign by Facebook test")
        self.assertTrue(True)
    def test_signupbytwitter(self):
        print("this is sighn by twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()