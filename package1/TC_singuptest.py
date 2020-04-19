import unittest


class LoginTest(unittest.TestCase):

    def test_signup_email(self):
        print("This is signup by email test")
        self.assertTrue(True)

    def test_signup_facebook(self):
        print("This is signup by facebook test")
        self.assertTrue(True)

    def test_signup_twitter(self):
        print("This is signup by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()