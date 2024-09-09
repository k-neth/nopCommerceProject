from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AddItemToCart:
    cart =""
    def __init__(self, driver):
        self.driver = driver

    def ClickCart(self):
        print("Cart Clicked")
        pass
    def ItemAdded(self):
        print("Item added to cart")
        pass
