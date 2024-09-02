import pytest
from pageObjects.LoginJumia import LoginJumia
from pageObjects.SearchItemJumia import SearchItemJumia
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from utilities.readCredentials import ReadConfig

@pytest.mark.usefixtures("setup")
class Test_J01:
    # baseurl = "https://www.kilimall.co.ke/login"
    # username="721356751"
    # password="@Kenya2023"
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    
        
    searchterm=ReadConfig.getSearchitem()
    # searchterm="Hennesy"

    # mdriver=webdriver.Chrome()

    @pytest.mark.regression
    def test_KilimallLogin(self):
                
        # self.driver = setup
       
        self.driver.get(self.baseurl)
        time.sleep(5)

        self.lp=LoginJumia(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
       




        # self.lp.CheckSuccess()
        # self.lp.searchitem(searchterm=self.searchterm)
        # self.lp.Startsearch()
        # self.lp.StartSearch()

    def test_KilimallSearch(self):
        # self.driver.get(self.baseurl)
  
        # self.test_KilimallLogin()
        self.ks=SearchItemJumia(self.driver)
        self.ks.Startsearch(searchterm=self.searchterm)
        self.ks.ClickSearchButton()
        # time.sleep(10)
        
        # self.ks.filterTop()
        # self.ks.ClickSearchButton()

    
   

        
        