import pytest
from pageObjects.LoginJumia import LoginJumia
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from utilities.readCredentials import ReadConfig

class Test_J01:
    # baseurl = "https://www.kilimall.co.ke/login"
    # username="721356751"
    # password="@Kenya2023"
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    searchterm="samsung"

    mdriver=webdriver.Chrome()

    @pytest.mark.regression
    def test_KilimallLogin(self):
        self.driver=self.mdriver
        self.driver.get(self.baseurl)
        time.sleep(5)

        self.lp=LoginJumia(mdriver=self.mdriver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.CheckSuccess()
        self.lp.searchitem(searchterm=self.searchterm)
        self.lp.Startsearch()
        # self.lp.StartSearch()
        
        