#1.打开浏览器
from selenium import  webdriver
driver=webdriver.Chrome()
#2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3.输入用户名
driver.find_element_by_id("username").send_keys("qing")
#4输入密码
driver.find_element_by_id("password").send_keys("123456")
#点击登陆按钮
#driver.find_element_by_class_name("login_btn").click()
driver.find_element_by_css_selector("input[class='login_btn fl']").click()



   