from selenium import  webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    title= "用户登录 - 道e坊商城 - Powered by Haidao"
    url="http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    loginbtn_click = (By.CLASS_NAME,"login_btn")
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys(username)

        self.driver.find_element(*self.username_input_loc).send_keys(username)


    def input_password(self,password):

        #self.driver.find_element(self.password_input_loc).send_keys(password)
    #def click_login_button(self):
        self.driver.find_element(*self.loginbtn_click).click()






