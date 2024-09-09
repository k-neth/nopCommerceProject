from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class GetPricesJumia:
    mainwrapperCSSSELECTOR=".listings"
    miniwrapperPriceCSSSelector=".product-price"

    def __init__(self, driver):
        self.driver=driver

    def getprices(self):
        miniwrapper=self.driver.find_element(By.CSS_SELECTOR,self.miniwrapperPriceCSSSelector).text
        print(miniwrapper)

