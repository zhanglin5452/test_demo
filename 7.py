# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_css_selector('#userA')
# sleep(2)
# driver.quit()
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# radios = driver.find_elements_by_xpath('//*[@type="radio"]')
# for i in range(len(radios)):
#     radios[i].click()
#     sleep(2)
# sleep(3)
# driver.quit()
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# driver.find_element_by_css_selector('#userA').send_keys('admin')
# sleep(1)
# driver.find_element_by_css_selector('#passwordA').send_keys('123456')
# sleep(1)
# driver.find_element_by_css_selector('#telA').send_keys('18611111111')
# sleep(1)
# driver.find_element_by_css_selector('#emailA').send_keys('545252568@qq.com')
# sleep(1)
# driver.find_element_by_css_selector('#telA').clear()
# sleep(1)
# driver.find_element_by_css_selector('#telA').send_keys('1860000000')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="zc"]/fieldset/button').click()
# sleep(2)
# driver.quit()
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('file:///C:/Users/86152/Desktop/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# userName = driver.find_element_by_xpath('//*[@id="userA"]').send_keys('admin')
# ActionChains(driver).double_click(userName).perform()
# sleep(2)
# btn = driver.find_element_by_xpath('//*[@id="zc"]/fieldset/button')
# ActionChains(driver).move_to_element(btn).perform()
# sleep(5)
# driver.quit()
# driver.find_element_by_xpath('//*[@id="zc"]/fieldset/p[10]/a').click()
# sleep(3)
#
# print(driver.current_url)
# print(driver.title)

# print(userA.text)
# print(userA.size)
# print(userA.get_attribute('for'))
# sleep(1)
# driver.quit()
from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('taobao')
# sleep(3)
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# sleep(3)
# driver.close()
# sleep(3)
# driver.quit()
# sleep(3)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(3)
# driver.quit()

# a = driver.find_element_by_xpath('//*[@id="cancelA"]')
# b = driver.find_element_by_xpath('//*[@id="zc"]/fieldset/p[5]')
# if a.is_enabled():
#     print('1')
# else:
#     print('0')
# if b.is_displayed():
#     print('1')
# else:
#     print('0')
# driver.quit()
# driver.maximize_window()
# driver.set_window_size(600,500)
# driver.set_window_position(500, 300)
# driver.set_window_rect(500,500,500,500)




# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
# D = driver.find_element_by_id('dragger')
# F = driver.find_element_by_xpath('/html/body/div[2]')
# ActionChains(driver).drag_and_drop(D, F).perform()
# sleep(3)
# driver.quit()



# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# name = driver.find_element_by_id('userA')
# name.send_keys('admin1')
# name.send_keys(Keys.BACK_SPACE)
# name.send_keys(Keys.CONTROL, 'a')
# name.send_keys(Keys.CONTROL, 'c')
# sleep(2)
# driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL, 'v')
# sleep(2)
# driver.quit()

# 需求：案例-1注册页面A,在用户名文本框上点击鼠标左键

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# user = driver.find_element_by_id('userA')
# ActionChains(driver).context_click(user).perform()


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# usera = driver.find_element_by_id('userA')
# usera.send_keys('admin')
# sleep(3)
# ActionChains(driver).double_click(usera).perform()
# sleep(3)
# driver.quit()
#
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8CA.html')
# but = driver.find_element_by_xpath('//*[@id="zc"]/fieldset/button')
# ActionChains(driver).move_to_element(but).perform()
# sleep(5)
# driver.quit()













