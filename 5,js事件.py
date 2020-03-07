from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.set_window_size(800,800)
js="window.scrollTo(200,450);"

driver.execute_script(js)
sleep(3)
driver.quit()

