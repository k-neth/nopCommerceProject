from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginJumia:
    username = "account"
    password = "password"
    loginbutton = "/html/body/div[1]/div/div[2]/div/div[1]/div/form/div[3]/button"
    searchtext="van-field-9-input"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.NAME, self.username).click()
        self.driver.find_element(By.NAME, self.username).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.password).send_keys(password)
        self.driver.find_element(By.NAME,self.password).send_keys(Keys.ENTER)
