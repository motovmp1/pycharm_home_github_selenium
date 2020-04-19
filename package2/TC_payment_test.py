import unittest


class PaymentTest(unittest.TestCase):

    def test_payment_dollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_payment_rupees(self):
        print("This is payment in rupees test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
