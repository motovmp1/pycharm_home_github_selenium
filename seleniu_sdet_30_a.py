import unittest
from selenium import webdriver
import time


class SearchEngine(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")
        self.driver.get("https://www.google.com.br/webhp?source=search_app")
        print("Open Google Page")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Title of the page is :" + self.driver.title)
        print("closing google...")
        time.sleep(5)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="/home/elsys/Documents/geckdriver_chrome/chromedriver")
        self.driver.get("https://www.bing.com")
        print("Open Bing Page")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("Title of the page is :" + self.driver.title)
        print("closing bing...")
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
