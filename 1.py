from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.taobao.com')
sleep(3)
driver.quit()


