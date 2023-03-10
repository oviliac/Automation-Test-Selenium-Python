import unittest
from unittest.suite import TestSuite
import register, login

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan ke test suite
    suite.addTest(tests.loadTestsFromModule(register))
    suite.addTest(tests.loadTestsFromModule(login))

    # run test suite
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


