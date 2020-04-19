import unittest
import time
from selenium import webdriver


class Test(unittest.TestCase):

    def test_alpha(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")
        driver.implicitly_wait(10)
        driver.maximize_window()
        title_of_page = driver.title
        print(title_of_page)
        time.sleep(2)
        self.assertEqual("Google", title_of_page, "Page is not the same")


if __name__ == "__main__":
    unittest.main()
