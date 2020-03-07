from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
sleep(3)
# driver.add_cookie({'name':'BAIDUID','value':'FD78BD12CEADD25FB7BC1FBD4F7F9289:FG=1'})
# driver.add_cookie({'name':'BDUSS','value':'ExRcjVPTkNSWGwzby1TN0VJeDh3VWhJZUZIVGdSMS1xdVdnMEY0RmttcndsREplRUFBQUFBJCQAAAAAAAAAAAEAAABidiDQuaS12LDh16nE3MrWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAHC17wBwteR'})
# driver.refresh()
# driver.find_element_by_id('kw').send_keys('123')
# driver.implicitly_wait(1)
web = WebDriverWait(driver, 10, 1).until(lambda s: driver.find_element_by_id('userA'))
web.send_keys('admin')
sleep(3)
driver.quit()