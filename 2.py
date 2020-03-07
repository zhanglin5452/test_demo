from selenium import webdriver
from time import sleep
# webdriver实例化浏览器
driver = webdriver.Chrome()
# 获取网址.get
driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
sleep(1)
# name定位元素
userA = driver.find_element_by_name('userA')
userA.send_keys('admin')
sleep(1)

pssA = driver.find_element_by_name('passwordA')

pssA.send_keys('123456')
sleep(1)
telA = driver.find_element_by_class_name('telA')
telA.send_keys('13594388458')
sleep(1)
# id便签定位元素
emalA = driver.find_element_by_id('emailA')
emalA.send_keys('545252568@qq.com')
sleep(1)
# link_text定位访问的网站
# xinlang = driver.find_element_by_link_text('访问 新浪 网站')
# xinlang.click()
driver.find_element_by_partial_link_text('访问 新浪 网站').click()

sleep(1)
driver.quit()