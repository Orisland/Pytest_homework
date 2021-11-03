import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    browser = webdriver.Chrome()
    browser.get("https://www.feed-the-beast.com/")


    def test_something(self):
        WebDriverWait(self.browser, 20).until(lambda get:self.browser.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div > div > div > div > div > div > div.level-left > div > p"))
        print("加载完成")
        # self.browser.find_element(By.CSS_SELECTOR, "#mpbutton-scaler > div:nth-child(1) > div.mpbutton-mask > a > img").click()



if __name__ == '__main__':
    unittest.main()
