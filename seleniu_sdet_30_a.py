import unittest
from selenium import webdriver
import time


class SearchEngine(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com.br/webhp?source=search_app")
        print("Open Google Page")
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Title of the page is :" + self.driver.title)
        time.sleep(5)
        print("closing google...")
        time.sleep(5)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.bing.com")
        time.sleep(2)
        print("Open Bing Page")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Title of the page is :" + self.driver.title)
        time.sleep(5)
        print("closing bing...")
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
