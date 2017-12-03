from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.execute_script("document.getElementsByClassName('site-nav-right fr')[0].childNodes[1].removeAttribute('target')")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("qing")
