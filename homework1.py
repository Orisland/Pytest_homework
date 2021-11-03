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
date:2021年11月02日08:02:09
"""

class MyTestCase(unittest.TestCase):
    keyword="属性测试"
    head = False

    @classmethod
    def setUpClass(self):
        timezone = str(time.time())
        self.name = str("q" + str(timezone).split(".", 1)[1])
        self.email = str(time.time()).split(".", 1)[0] + "@qq.com"
        self.password = "zhaolong123"
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # I don't want to see the page.
        if self.head:
            self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        else:
            self.browser = webdriver.Chrome()
        self.browser.get("https://ecshop.test2.shopex123.com")
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()

    def test_reg(self): # reg
        print("reg start")
        # 显示调用弃用，太费劲了。
        self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > a.reg").click()
        self.browser.find_element(By.CSS_SELECTOR, "#username").send_keys(self.name)
        self.browser.find_element(By.CSS_SELECTOR, "#email").send_keys(self.email)
        self.browser.find_element(By.CSS_SELECTOR, "#password1").send_keys(self.password)
        self.browser.find_element(By.CSS_SELECTOR, "#confirm_password").send_keys(self.password)
        self.browser.find_element(By.CSS_SELECTOR, "#main > div.content_body > form > div.act > input.signup_button").click()
        self.assertTrue("成功" in self.browser.find_element(By.CLASS_NAME, "block").text)
        print("reg pass")

    def test_login(self):
        print("login start")
        if(self.name in self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > font > font").text):
            self.assertTrue(self.name in self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > font > font").text)
            print("login pass")
        else:
            self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > a.sign").click()
            self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > div:nth-child(1) > div > input").send_keys(self.name)
            self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > div:nth-child(2) > div > input").send_keys(self.password)
            self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > input.loginbtn").click()
            self.assertTrue("成功" in self.browser.find_element(By.CLASS_NAME, "block").text)
            print("login pass")

    def test_login_dir(self):
        print("login_dir start")
        if(self.name in self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > font > font").text):
            self.logout()
        self.browser.find_element(By.CSS_SELECTOR, "#ECS_MEMBERZONE > a.sign").click()
        self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > div:nth-child(1) > div > input").send_keys(self.name)
        self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > div:nth-child(2) > div > input").send_keys(self.password)
        self.browser.find_element(By.CSS_SELECTOR, "#body > div.loginWrap > div > div.loginBord > form > input.loginbtn").click()
        self.assertTrue("成功" in self.browser.find_element(By.CLASS_NAME, "block").text)
        print("login_dir pass")

    def logout(self):   #刷新浏览器数据重新登入
        print("logout")
        if self.head:
            self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        else:
            self.browser = webdriver.Chrome()
        self.browser.get("https://ecshop.test2.shopex123.com")
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()

    def shutdown(self):
        self.browser.close()

    def test_search(self):
        print("search start")
        self.browser.find_element(By.CSS_SELECTOR, "#keyword").send_keys(self.keyword)
        self.browser.find_element(By.CSS_SELECTOR, "#searchForm > table > tbody > tr > td:nth-child(2) > input").click()

        i = 0
        while True:
            if len(self.keyword) > 30:
                self.keyword = str(self.keyword)[0:29]
            a = self.browser.find_element(By.PARTIAL_LINK_TEXT, self.keyword)
            if a is None:
                self.browser.find_element(By.CSS_SELECTOR, "#pager > span > a:nth-child(3)").click()
            else:
                break
            i += 1
            if i > 10:
                print("寻找10页未找到")
                print("该商品不存在")
                self.assertTrue(True, False)
                break
        a.click()
        self.assertTrue(self.keyword in self.browser.find_element(By.CSS_SELECTOR, "#goodsInfo > div.textInfo > div.goodsnames").text)
        print("search pass")

    def test_addbuycar(self):
        print("addbuycar start")
        self.browser.find_element(By.CSS_SELECTOR, "#ECS_FORMBUY > ul > li.padd.loop > label:nth-child(3)").click()
        self.browser.find_element(By.CSS_SELECTOR, "#com_b > a").click()
        self.assertTrue("成功" in self.browser.find_element(By.CSS_SELECTOR, "#speDiv > div.conclose > span").text)
        print("addbuycar pass")

    def test_detail(self):
        print("detail start")
        self.browser.find_element(By.CSS_SELECTOR, "#speDiv > div.cartpopDiv > div.fd30_btn > a.bg_c.fd_submit").click()
        Select(self.browser.find_element(By.CSS_SELECTOR, "#selCountries_0")).select_by_index(1)    # 中国
        Select(self.browser.find_element(By.CSS_SELECTOR, "#selProvinces_0")).select_by_value("13")   # 安徽
        Select(self.browser.find_element(By.CSS_SELECTOR, "#selCities_0")).select_by_value("144")  # 阜阳
        Select(self.browser.find_element(By.CSS_SELECTOR, "#selDistricts_0")).select_by_value("1541")  # 颍州
        self.browser.find_element(By.CSS_SELECTOR, "#consignee_0").send_keys("Orisland")
        self.browser.find_element(By.CSS_SELECTOR, "#address_0").send_keys("美利坚合众国纽约州")
        self.browser.find_element(By.CSS_SELECTOR, "#tel_0").send_keys("0558-911")
        self.browser.find_element(By.CSS_SELECTOR, "#mobile_0").send_keys("19994641992")
        self.browser.find_element(By.CSS_SELECTOR, "#sign_building_0").send_keys("世界贸易中心一号楼")
        self.browser.find_element(By.CSS_SELECTOR, "#zipcode_0").send_keys("236000")
        self.browser.find_element(By.CSS_SELECTOR, "#best_time_0").send_keys("2000-9-11")
        self.browser.find_element(By.CSS_SELECTOR, "#theForm > div > table > tbody > tr:nth-child(6) > td > input.bnt_blue_2").click()
        self.assertTrue("费用总计" in self.browser.find_element(By.CSS_SELECTOR, "#theForm > div:nth-child(17) > h6 > span").text)
        print("detail pass")


    def test_paycheck(self):
        self.browser.find_element(By.CSS_SELECTOR, "#shippingTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]").click()
        self.browser.find_element(By.CSS_SELECTOR, "#paymentTable > tbody > tr:nth-child(5) > td:nth-child(1) > input[type=radio]").click()
        self.browser.find_element(By.CSS_SELECTOR, "#packTable > tbody > tr:nth-child(3) > td:nth-child(1) > input[type=radio]").click()
        self.browser.find_element(By.CSS_SELECTOR, "#cardTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]").click()
        self.browser.find_element(By.CSS_SELECTOR, "#theForm > div:nth-child(17) > div:nth-child(4) > input[type=image]:nth-child(1)").click()
        self.assertTrue("成功" in self.browser.find_element(By.CSS_SELECTOR, "body > div.block > div.flowBox > h6 > font:nth-child(1)").text)


    @classmethod
    def tearDownClass(cls):
        cls.shutdown(self=cls)

if __name__ == '__main__':
    # testSuite = unittest.TestSuite()
    # testSuite.addTest(MyTestCase('test_reg'))
    # testSuite.addTest(MyTestCase('test_login'))
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_reg"))
    suite.addTest(MyTestCase("test_login"))
    suite.addTest(MyTestCase("test_login_dir"))
    suite.addTest(MyTestCase("test_search"))
    suite.addTest(MyTestCase("test_addbuycar"))
    suite.addTest(MyTestCase("test_detail"))
    suite.addTest(MyTestCase("test_paycheck"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


    # unittest.main()
