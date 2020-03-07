from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
element = driver.find_element_by_id('selectA')
select = Select(element)
# for i in range(4):
#     select.select_by_index(i)
#     sleep(2)
list = ['A北京', 'A上海', 'A广州', 'A重庆']
for i in list:
    select.select_by_visible_text(i)
    sleep(2)
driver.quit()