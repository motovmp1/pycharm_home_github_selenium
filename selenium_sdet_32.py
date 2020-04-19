import unittest
import time


class AppTesting(unittest.TestCase):

    def test_search1(self):
        print(" This is test searching number 1")

    @unittest.SkipTest
    def test_search2(self):
        print(" This is test searching number 2")

    def test_search3(self):
        print(" This is test searching number 3")

    def test_search4(self):
        print(" This is test searching number 4")

    def test_search5(self):
        print(" This is test searching number 5")

    def test_search6(self):
        print(" This is test searching number 6")


if __name__ == "__main__":
    unittest.main()
