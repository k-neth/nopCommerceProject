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

    def __init__(self, mdriver):
        self.driver = mdriver

    def setUsername(self,username):
        self.driver.find_element(By.NAME, self.username).click()
        self.driver.find_element(By.NAME, self.username).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.password).send_keys(password)
        self.driver.find_element(By.NAME,self.password).send_keys(Keys.ENTER)
    def CheckSuccess(self):
        global startsearch
        startsearch=self.driver.find_element(By.ID, self.searchtext)
        startsearch.click()
    def searchitem(self,searchterm):
    
        startsearch.send_keys(searchterm)
    def Startsearch(self):
        startsearch.click()
        startsearch.send_keys(Keys.ENTER)
    # def StartSearch(self):
    #     startsearch.send_keys(Keys.ENTER)
        
        

        # WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(self.driver.find_element(By.XPATH, self.searchtext)))
       


    # def clickLogin(self):
    #     self.driver.find_element(By.XPATH,self.loginbutton).click()