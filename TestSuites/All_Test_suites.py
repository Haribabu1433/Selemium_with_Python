import unittest
from package1.TC_loginTest import LoginTest
from package1.TC_SignupTest import Signuptest
from package2.TC_PaymentTest import Paymenttest
from package2.TC_PaymentReturns import PaymentReturn


# get all tests from LoginTest,SignupTest,Paymenttest,Payement Return
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Signuptest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Paymenttest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

# creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2]) # sanity test suite
FunctionalTestSuite = unittest.TestSuite([tc3,tc4]) # Functional test suite
MasterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4]) # Master Test suite

#unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(FunctionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(MasterTestSuite) # verbosity=2 for detailed log


