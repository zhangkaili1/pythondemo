import  unittest

import time

import ddt
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read

@ddt.ddt
class MemberManageTest(unittest.TestCase):
    member_info = read("member_info.csv")
    @classmethod
    def  setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
    def test_a_log_in(self):
         print("登陆测试")
         driver=self.driver
         driver.get("http://localhost/admin.php")
         driver.find_element_by_name("username").send_keys("admin")
         ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1111").send_keys(Keys.ENTER).perform()

    @ddt.data(*member_info)
    def testb_add_member(self, row):
        driver = self.driver
        # for循环不太好，推荐使用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行的目的
        # ddt是数据驱动测试 data driver test
        # 注释掉for循环，改变代码的缩进 shift+tab  使方法中的代码比方法声明缩进4个空格
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector("[value='" + row[2] + "']").click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        # if actual == expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")
        # driver.find_element_by_class_name("button_search").click()

        # 切换到父框架
        #driver.switch_to.parent_frame()
        self.assertEqual(actual, expected)
        # 切换到网页的根节点
        driver.switch_to.default_content()
if __name__ == '__main__':
    unittest.main()




