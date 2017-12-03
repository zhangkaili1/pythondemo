from selenium import  webdriver
import time
#45版本以下的firefox浏览器，不需要驱动文件
#46版本开始的fireFox浏览器，需要driver.exe文件放到环境变量下面
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.implicitly_wait(30)
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("qing")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
#time.sleep(5)
driver.find_element_by_css_selector(".kong a[href='/index.php']").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphone_img =""
#driver.find_elements_by_css_selector(".shop_01-imgbox  img")[0].click()
link_img =  driver.find_element_by_css_selector("div.shop_01-imgbox>a")
driver.execute_script("arguments[0].removeAttribute('target')",link_img)
link_img.click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("aaa")
driver.find_element_by_name("address[mobile]").send_keys("123465789")
#driver.find_element_by_id("add-new-area-select").find_element_by_css_selector("option[value='130000']").click()
Select(driver.find_element_by_id("add-new-area-select")).select_by_value("320000")
Select(driver.find_elements_by_css_selector("select")[1]).select_by_value("320200")
Select(driver.find_elements_by_css_selector("select")[2]).select_by_value("320202")
#Select(driver.find_element_by_id("add-new-area-select")).select_by_value("320202")
#address[address]
driver.find_element_by_name("address[address]").send_keys("qwqeq")
driver.find_element_by_name("address[zipcode]").send_keys("123456")
driver.find_element_by_class_name("aui_state_highlight").click()




