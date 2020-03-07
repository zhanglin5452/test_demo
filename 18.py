from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('file:///C:/Users/86152/Desktop/web%E8%87%AA%E5%8A%A8%E5%8C%96-Day02/01-%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/sucai/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')
driver.find_element_by_link_text('注册A网页').click()
all_windowA = driver.window_handles
windowA = all_windowA[1]
driver.switch_to.window(windowA)
driver.find_element_by_name('userA').send_keys('admin')
driver.maximize_window()
driver.get_screenshot_as_file('a.png')
sleep(2)
driver.quit()

