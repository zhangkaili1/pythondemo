import unittest

import time
from selenium import  webdriver
class MemberManageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()
    def test_addMember(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1111")
        driver.find_element_by_class_name("Btn").click()
        driver.find_elements_by_css_selector("div.menu.fl>a")[3].click()
        #driver.find_element_by_css_selector("div.side>ul:nth-child(3)>li:nth-child(3)>a").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("123456")
        driver.find_element_by_name("mobile_phone").send_keys("13800383015")
        driver.find_element_by_css_selector("[value='0']").click()
        driver.find_element_by_id("birthday").send_keys("2017-11-24")
        driver.find_element_by_name("email").send_keys("1452@qq.com")
        driver.find_element_by_name("qq").send_keys("12456789")
        driver.find_element_by_class_name("button_search").click()


