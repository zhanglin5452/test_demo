# from selenium import webdriver
# # from time import sleep
# # driver = webdriver.Chrome()
# # driver.get('http://sahitest.com/demo/alertTest.htm')
# # user = driver.find_element_by_name('b1')
# # user.click()
# # sleep(2)
# # alet = driver.switch_to.alert
# # print(alet.text)
# # alet.accept()
# # sleep(2)
# # driver.quit()
# from selenium import webdriver
# from  time import sleep
# driver = webdriver.Firefox()
# driver.get('http://sahitest.com/demo/promptTest.htm')
# els = driver.find_element_by_name('b1')
# els.click()
# sleep(2)
# po = driver.switch_to.alert
# po.send_keys('你好')
# sleep(2)
# po.accept()
# sleep(2)
# driver.quit()
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# driver.get('http://www.taobao.com/')
# # js = 'window.scrollTo(0,10000)'
# # driver.execute_script(js)
# # sleep(3)
# for i in range(0,100000,5000):
#     js = 'window.scrollTo(0,%d)'% i
#     sleep(2)
#     driver.execute_script(js)
# sleep(1)
# driver.quit()