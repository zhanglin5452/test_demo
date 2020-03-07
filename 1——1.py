from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('http://www.yhd.com/')
driver.find_element_by_partial_link_text('登录').click()
driver.implicitly_wait(5)
driver.find_element_by_id('un').send_keys('zhanglin5452')
driver.find_element_by_id('pwd').send_keys('545252568zl')
sleep(2)
driver.find_element_by_id('login_button').click()
try:
    abc = driver.find_element_by_xpath("//*[text()='账号和密码不匹配，请重新输入']")
    assert True
except Exception:
    assert False