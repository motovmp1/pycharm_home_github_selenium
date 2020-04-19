import unittest
import time
from selenium import webdriver


class Test(unittest.TestCase):
    driver = webdriver.Firefox()

    def test_name(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.maximize_window()

    def test_get_title_page(self):
        title_of_page = self.driver.title
        self.assertEqual("Google", title_of_page, "Page is not the same")


if __name__ == "__main__":
    unittest.main()
