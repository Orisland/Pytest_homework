import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
author:zhaolong
date:2021年11月02日15:04:34
"""

in_out = 1
class MyTestCase(unittest.TestCase):
    keyword = "属性测试"
    head = False
    sleepTime = 4
    global in_out

    def test_1_login(self):
        print("login")
        WebDriverWait(self.browser, 20).until(lambda browser: self.browser.find_element(By.CSS_SELECTOR, "#user_reg > div.form-group.m-t-10 > div:nth-child(3) > a"))
        self.browser.find_element(By.CSS_SELECTOR, "#user_reg > div.form-group.m-t-10 > div:nth-child(3) > a").click()
        WebDriverWait(self.browser, 20).until(lambda browser: self.browser.find_element(By.CSS_SELECTOR, "#btnOk"))
        self.browser.find_element(By.CSS_SELECTOR, "#btnOk").click()

        WebDriverWait(self.browser, 20).until(lambda get: self.browser.find_element(
            By.CSS_SELECTOR, "#layui-layer1 > div.layui-layer-btn.layui-layer-btn-c > a"))
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "#layui-layer1 > div.layui-layer-btn.layui-layer-btn-c > a").click()

        self.assertTrue("欢迎" in self.browser.find_element(By.CSS_SELECTOR, "body > div.layui-layout.layui-layout-admin.okadmin.blue_theme > div.layui-side.layui-side-menu.okadmin-bg-20222A.ok-left > div > div.user-photo > p").text)
        print("login pass")

    def test_2_input(self):
        print("input")
        self.test_1_login()

        self.browser.find_element(By.XPATH, "//*[@id='navBar']/li[3]/a").click()
        self.browser.find_element(By.CSS_SELECTOR, "#navBar > li.layui-nav-item.layui-nav-itemed > dl > dd:nth-child(1) > a").click()
        # time.sleep(self.sleepTime)
        WebDriverWait(self.browser, 20).until(lambda get: self.browser.find_element(By.CSS_SELECTOR, "#tabContent > div.layui-tab-item.layui-show > iframe"))
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#tabContent > div.layui-tab-item.layui-show > iframe")
        self.browser.switch_to.frame(iframe)
        print("切换iframe0")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "body > div > div > div.layui-table-tool > div.layui-table-tool-temp > div > button.layui-btn.layui-btn-sm.layui-btn-normal").click()
        print("按钮单机完成")
        WebDriverWait(self.browser, 20).until(lambda get: self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1"))
        # time.sleep(self.sleepTime)
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1")
        self.browser.switch_to.frame(iframe)
        print("切换iframe")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > div > input").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "body > fieldset:nth-child(6) > div:nth-child(2) > button").click()
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1")
        self.browser.switch_to.frame(iframe)
        print("切换iframe")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR, "body > div > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-r > div.layui-table-body > table > tbody > tr:nth-child(6) > td > div > a").click()
        self.browser.switch_to.parent_frame()
        print("切换iframe")
        self.browser.find_element(By.CSS_SELECTOR, "#layui-layer1 > span.layui-layer-setwin").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div > input").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > dl > dd:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#originalcode").send_keys("123123123")
        self.browser.find_element(By.CSS_SELECTOR, "#note").send_keys("note note note")
        self.browser.find_element(By.CSS_SELECTOR, "#custname").send_keys("aaa")
        billcode = self.browser.find_element(By.CSS_SELECTOR, "#billcode").text
        self.browser.find_element(By.CSS_SELECTOR, "body > div > div > div:nth-child(1) > button").click()
        self.browser.switch_to.parent_frame()
        print("切换iframe")
        self.assertTrue(billcode in self.browser.find_element(By.CSS_SELECTOR, "body > div.ok-body > div > div.layui-table-box > div.layui-table-body.layui-table-main > table > tbody").text)
        print("input pass")

    def test_3_output(self):
        self.test_1_login()
        print("output")
        self.browser.find_element(By.XPATH, "//*[@id='navBar']/li[4]/a").click()
        self.browser.find_element(By.CSS_SELECTOR, "#navBar > li.layui-nav-item.layui-nav-itemed > dl > dd:nth-child(1) > a").click()
        # time.sleep(self.sleepTime)
        WebDriverWait(self.browser, 20).until(lambda get: self.browser.find_element(By.CSS_SELECTOR, "#tabContent > div.layui-tab-item.layui-show > iframe"))
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#tabContent > div.layui-tab-item.layui-show > iframe")
        self.browser.switch_to.frame(iframe)
        print("切换iframe0")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "body > div.ok-body > div > div.layui-table-tool > div.layui-table-tool-temp > div > button.layui-btn.layui-btn-sm.layui-btn-normal").click()
        print("按钮单机完成")
        WebDriverWait(self.browser, 20).until(lambda get: self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1"))
        # time.sleep(self.sleepTime)
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1")
        self.browser.switch_to.frame(iframe)
        print("切换iframe")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > div > input").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "body > fieldset:nth-child(6) > div:nth-child(2) > button").click()
        iframe = self.browser.find_element(By.CSS_SELECTOR, "#layui-layer-iframe1")
        self.browser.switch_to.frame(iframe)
        print("切换iframe")
        time.sleep(self.sleepTime)
        self.browser.find_element(By.CSS_SELECTOR, "body > div > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-r > div.layui-table-body > table > tbody > tr:nth-child(6) > td > div > a").click()
        self.browser.switch_to.parent_frame()
        print("切换iframe")
        self.browser.find_element(By.CSS_SELECTOR, "#layui-layer1 > span.layui-layer-setwin").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div > input").click()
        self.browser.find_element(By.CSS_SELECTOR, "#bill_info > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > dl > dd:nth-child(2)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#originalcode").send_keys("123123123")
        self.browser.find_element(By.CSS_SELECTOR, "#note").send_keys("note note note")
        self.browser.find_element(By.CSS_SELECTOR, "#custname").send_keys("aaa")
        billcode = self.browser.find_element(By.CSS_SELECTOR, "#billcode").text
        self.browser.find_element(By.CSS_SELECTOR, "body > div > div > div:nth-child(1) > button").click()
        self.browser.switch_to.parent_frame()
        print("切换iframe")
        self.assertTrue(billcode in self.browser.find_element(By.CSS_SELECTOR, "body > div.ok-body > div > div.layui-table-box > div.layui-table-body.layui-table-main > table > tbody").text)
        print("output pass")


    # def

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # I don't want to see the page.
        if self.head:
            self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        else:
            self.browser = webdriver.Chrome()
        self.browser.get("http://t.lenoyun.com/ydepot/public/login?type=reg")
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)


        # print("input pass")
    def find_element(self, selector):
        WebDriverWait(self.browser, 20, 0.5).until(lambda get: self.browser.find_element(By.CSS_SELECTOR, selector))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_1_login"))
    suite.addTest(MyTestCase("test_2_input"))
    suite.addTest(MyTestCase("test_3_output"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

