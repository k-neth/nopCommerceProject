from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SearchItemJumia:
    searchtext="van-field-9-input"
    searchbutton = ".search-button"
    # filtertopsales="//*[@id='__nuxt']/div/div[3]/div[2]/div[2]/div[1]/div[2]/span"

    def __init__(self, driver):
        self.driver = driver

    # def CheckSuccess(self):
        
    #     startsearch=self.driver.find_element(By.ID, self.searchtext)
    #     startsearch.click()
    # def searchitem(self,searchterm):
    
    #     startsearch.send_keys(searchterm)
    def Startsearch(self,searchterm):
        startsearch=self.driver.find_element(By.ID, self.searchtext)

        startsearch.click()
        startsearch.send_keys(searchterm)
    def ClickSearchButton(self):
        submit=self.driver.find_element(By.CSS_SELECTOR, self.searchbutton)
        submit.click()
    # def filterTop(self):
    #     mysearchfilter=self.driver.find_element(By.XPATH, self.filtertopsales)
    #     mysearchfilter.click()

    
        # startsearch.send_keys(Keys.DOWN)
        # startsearch.send_keys(Keys.ENTER)
