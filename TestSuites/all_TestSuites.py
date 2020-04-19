import unittest

from package1.TC_loginTest import LoginTest
from package1.TC_singuptest import SignupTest

from package2.TC_payment_test import PaymentTest
from package2.TC_payment_return import PaymentReturn


TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)


# Sanity test case suites
sanityTestSuite = unittest.TestSuite([TC1, TC2])
# unittest.TextTestRunner().run(sanityTestSuite)


# Functional test suite case
functional_test = unittest.TestSuite([TC3, TC4])
# unittest.TextTestRunner().run(functional_test)


# Master test Suite case
master_suite = unittest.TestSuite([TC1, TC2, TC3, TC4])
unittest.TextTestRunner(verbosity=2).run(master_suite)


'''
    verbosity = 2
    0 (quiet): you just get the total numbers of tests executed and the global result
    1 (default): you get the same plus a dot for every successful test or a F for every failure
    2 (verbose): you get the help string of every test and the result

'''