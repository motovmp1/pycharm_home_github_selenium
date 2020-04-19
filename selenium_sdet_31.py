import unittest
from selenium import webdriver
import time


class SearchEngine(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get("https://www.google.com.br/webhp?source=search_app")
        print("Open Google Page")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_title(self):
        time.sleep(2)
        print("Title of the page is :" + self.driver.title)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print("closing navigator...")
        time.sleep(5)
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
