import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HTMLTestRunner
import time


"""
author:wdr
"""

class EcshopUseTest(unittest.TestCase):

    # 自动加载姓名，邮箱信息
    base = str(time.time())
    name = str(base).split(".", 1)[1]
    email = str(time.time()) + r"@qq.com"

    def setUp(self):    #每条用力执行前的操作
        self.browser = webdriver.Chrome()
        self.browser.get("https://ecshop.test2.shopex123.com")
        self.browser.implicitly_wait(6)
        self.browser.maximize_window()

    # def tearDown(self):     #每条用例执行后的操作
    #     self.browser.quit()

    def test_userRegiser(self):
        """测试自动注册"""
        self.browser.find_element(By.PARTIAL_LINK_TEXT,"免费注册").click()
        self.browser.find_element(By.ID,"username").send_keys(self.name)
        self.browser.find_element(By.ID,"email").send_keys(self.email)
        self.browser.find_element(By.ID,"password1").send_keys("123456wdr")
        self.browser.find_element(By.ID,"confirm_password").send_keys("123456wdr")
        self.browser.find_element(By.NAME,"extend_field3").send_keys("13379612666")
        self.browser.find_element(By.NAME,"extend_field113").send_keys("圆环之理")
        self.browser.find_element(By.NAME,"Submit").click()
        #判断是否成功
        msg = self.browser.find_element(By.CLASS_NAME, "f4").text
        self.assertTrue(self.name in msg)  # 断言是否注册成功

    def test_userLogon(self):
        """登录测试"""
        self.browser.find_element(By.PARTIAL_LINK_TEXT,"请登录").click()
        self.browser.find_element(By.NAME,"username").send_keys(self.name)
        self.browser.find_element(By.NAME, "password").send_keys("123456wdr")
        self.browser.find_element(By.NAME, "submit").click()
        #判断是否成功
        msg = self.browser.find_element(By.CLASS_NAME, "f4_b").text
        self.assertTrue(self.name in msg)  # 断言是否注册成功

    def test_searchGoods(self):
        # 登录及搜索页面
        self.test_userLogon()
        self.browser.find_element(By.ID,"keyword").send_keys("眼霜")
        self.browser.find_element(By.NAME, "imageField").click()
        self.browser.find_element(By.PARTIAL_LINK_TEXT,"风姿三件套乳霜和").click()
        self.browser.find_element(By.XPATH,"//li[@class='padd']/a[@class='addToCart']").click()
        # self.browser.execute_script("document.evaluate(//li[@class='padd']/a[@class='addToCart').click")
        self.browser.find_element(By.LINK_TEXT,"去结算").click()



        # 地址选择页面
        self.browser.find_element(By.XPATH,"//select[@id='selProvinces_0']/option[3]").click()
        self.browser.find_element(By.XPATH,"//select[@id='selCities_0']/option[2]").click()
        self.browser.find_element(By.XPATH,"//select[@id='selDistricts_0']/option[3]").click()

        # 地址输入页面
        self.browser.find_element(By.ID,"consignee_0").send_keys("wdr")
        self.browser.find_element(By.ID,"address_0").send_keys("柳州工学院")
        self.browser.find_element(By.ID,"zipcode_0").send_keys("558200")
        self.browser.find_element(By.ID,"tel_0").send_keys("13379612541")
        self.browser.find_element(By.ID, "mobile_0").send_keys("13379612541")
        self.browser.find_element(By.ID,"sign_building_0").send_keys("离子研究中心")
        self.browser.find_element(By.ID,"best_time_0").send_keys("2021年12月12日")
        self.browser.find_element(By.NAME,"Submit").click()

        # 支付方式及快递方式选择
        self.browser.find_element(By.XPATH,"//table[@id='shippingTable']/tbody/tr[2]/td[@valign='top']/input[@name='shipping']").click()
        self.browser.find_element(By.XPATH,"//table[@id='paymentTable']/tbody/tr[4]/td[1]/input").click()
        self.browser.find_element(By.XPATH,"//div[@align='center']/input[@type='image']").click()






if __name__ == '__main__':

    testSuite = unittest.TestSuite()
    testSuite.addTests([EcshopUseTest("test_userRegiser")])
    # testSuite.addTests([EcshopUseTest("test_userLogon")])
    testSuite.addTests([EcshopUseTest("test_searchGoods")])

    fileName=str(time.time())
    print(fileName)
    file=open(r"/Users/zhaolong/Desktop/pythonTest"+fileName+".html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = file,
                                           title="自动化测试报告",
                                           description="注册接口报告",
                                           )
    runner.run(testSuite)
    file.close()
