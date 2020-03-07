from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
driver.find_element_by_css_selector('#userA').send_keys('admin')
sleep(1)
driver.find_element_by_css_selector('#passwordA').send_keys('123456')
sleep(1)
driver.find_element_by_css_selector('#telA').send_keys('135943885420')
sleep(1)
driver.find_element_by_css_selector('#emailA').send_keys('545252568@qq.com')
sleep(2)
zhuce = driver.find_element_by_tag_name('button')
ActionChains(driver).double_click(zhuce).perform()

sleep(2)
driver.quit()