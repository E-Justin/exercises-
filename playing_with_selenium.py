from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc  # need this to bypass google login
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")  # driver path

driver.get('https://amazon.com')  # go to amazon.com
time.sleep(5)  # wait 5 seconds
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')  # search bar
search_bar.send_keys('mechanical keyboard')  # type in mechanical keyboard
search_bar.send_keys(Keys.RETURN)  # hit enter

high_price_input = driver.find_element(
    By.ID, 'high-price')  # find high price input box
high_price_input.send_keys('50.00')  # type in 50
high_price_input.send_keys(Keys.RETURN)  # hit enter


time.sleep(5)  # wait 5 seconds
