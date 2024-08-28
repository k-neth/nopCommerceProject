from selenium import webdriver
import undetected_chromedriver as uc

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
driver.get('https://admin-demo.nopcommerce.com/')
print(driver.title)
driver.quit()
