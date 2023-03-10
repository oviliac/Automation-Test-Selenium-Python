import unittest
from unittest.suite import TestSuite
import register, login, cart

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan ke test suite
    suite.addTest(tests.loadTestsFromModule(register))
    suite.addTest(tests.loadTestsFromModule(login))
    suite.addTest(tests.loadTestsFromModule(cart))

    # run test suite
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


