import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("qing")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("你好")
driver.find_element_by_css_selector("input[value='2']").click()
date = "document.getElementById('date').removeAttribute('readonly')"
driver.execute_script(date)
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("2012-05-01")
driver.find_element_by_id("qq").send_keys("1587895")
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
driver.switch_to.alert.accept()

