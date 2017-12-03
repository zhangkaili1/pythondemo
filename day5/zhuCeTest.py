import os

from  selenium import  webdriver

from day5 import myTestCase
from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
     def test_zhu_ce(self):
         driver = self.driver
         driver.get("http://localhost/index.php?m=user&c=public&a=reg")
         actual = driver.title
         expected ="用户注册 - 道e坊商城 - Powered by Haidao"
         basepath = os.path.dirname(__file__)
         path = basepath.replace("day5","report/img/")
         driver.get_screenshot_as_file(path +"zhuce.png")
         self.assertEqual(actual,expected)


