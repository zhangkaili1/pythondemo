import time
from selenium import  webdriver

from day5.myTestCase import MyTestCase
from day6.loginPage import LoginPage


class LoginTest(MyTestCase):
    def test_login(self):
        lp=LoginPage(self.driver)
        lp.open()
        lp.input_username("qing")
       # lp.input_password("123456")
        #lp.click_login_button()
        #pcp=PersonalCenterPage()
       # pcp.assertEqual(pcp.title,self.driver.title)
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 3.输入用户名
        #self.driver.find_element_by_id("username").send_keys("qing")
        # 4输入密码
        #self.driver.find_element_by_id("password").send_keys("123456")
        # 点击登陆按钮
        # driver.find_element_by_class_name("login_btn").click()
        #self.driver.find_element_by_css_selector("input[class='login_btn fl']").click()
        #actual = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        #time.sleep(5)
        #self.assertIn("我的会员中心",self.driver.title)





