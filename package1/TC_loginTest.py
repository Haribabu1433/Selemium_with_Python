import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyemail(self):
        print("this is loging test")
        self.assertTrue(True)
    def test_loginbyFacebook(self):
        print("this is loging test")
        self.assertTrue(True)
    def test_Loginbytwitter(self):
        print("this is loging test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()