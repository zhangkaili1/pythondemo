import time
from selenium import  webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.implicitly_wait(30)
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1111")
driver.find_element_by_class_name("Btn").click()
driver.find_elements_by_css_selector("div.menu.fl>a")[1].click()
#driver.find_elements_by_css_selector("div.side>ul>li")[1].click()
driver.find_element_by_css_selector("div.side>ul:nth-child(3)>li:nth-child(2)>a").click()
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("1231")
driver.find_element_by_css_selector("div.fenlei>div.fendd.clearfix>div:nth-child(1)>a:nth-child(1)").click()
driver.find_element_by_css_selector("div.fenlei>div.fendd.clearfix>div:nth-child(2)>a:nth-child(1)").click()
driver.find_element_by_css_selector("div.fenlei>div.fendd.clearfix>div:nth-child(3)>a:nth-child(1)").click()
#driver.find_element_by_css_selector("div.fenlei>div.fendd.clearfix>div:nth-child(4)>a:nth-child(1)").click()
#driver.find_element_by_id("jiafen").click()
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
driver.find_element_by_css_selector("option[value='1']").click()
driver.find_element_by_css_selector("input[value='1']").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_link_text("商品图册").click()
#ActionChains(driver).click(driver.find_element_by_class_name("webuploader-pick")).perform()
driver.find_element_by_name("file").send_keys("D:/1.png")
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
time.sleep(1)
driver.switch_to.alert.accept()
#driver.find_element_by_class_name("button_search").click()


