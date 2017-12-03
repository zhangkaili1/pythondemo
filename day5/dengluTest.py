import  unittest
from selenium import  webdriver

class DengLuTest(unittest.TestCase):
    """登陆模块测试用例"""
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_denglu(self):
        """登陆正常测试用例"""
        driver= self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 3.输入用户名
        driver.find_element_by_id("username").send_keys("qing")
        # 4输入密码
        driver.find_element_by_id("password").send_keys("123456")
        # 点击登陆按钮
        # driver.find_element_by_class_name("login_btn").click()
        driver.find_element_by_css_selector("input[class='login_btn fl']").click()
        print("..")