#打开浏览器
from selenium import  webdriver
driver = webdriver.Chrome()
#打开海盗商城的主页
driver.get("http://localhost/")
#点击注册链接
driver.find_element_by_link_text("注册").click()
cwh = driver.current_window_handle
for item in driver.window_handles:
    if item==cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_name("username").send_keys("qing123")


#