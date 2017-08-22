from selenium import webdriver
import time

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/")
    def find_element(self):
        self.driver.find_element_by_xpath("//*[@id='content']/ul/li[18]/a").click()
    def login(self, params):
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(params.email)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(params.password)
        self.driver.find_element_by_xpath("//*[@id='login']/button/i").click()
        time.sleep(5)
    def screenshot(self):
        self.driver.get_screenshot_as_file("my_task.png")
    def driver_close(self):
        self.driver.close()