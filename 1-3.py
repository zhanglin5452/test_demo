import unittest
from selenium import webdriver
from time import sleep
class Test_Log(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.yhd.com/')
        self.driver.find_element_by_partial_link_text('登录').click()
        sleep(2)
    def tearDown(self):
         self.driver.quit()
    def test_Login_sucess(self):
        self.driver.find_element_by_id('un').send_keys('zhanglin5452')
        self.driver.find_element_by_id('pwd').send_keys('545252568zl')
        self.driver.find_element_by_id('login_button').click()
        try:
             self.driver.find_element_by_xpath("//*[text()='zhanglin5452']")
             assert True
        except Exception:
            assert False
    def test_Login_fail(self):
        self.driver.find_element_by_id('un').send_keys('zhanglin5452')
        self.driver.find_element_by_id('pwd').send_keys('545252568')
        self.driver.find_element_by_id('login_button').click()
        try:
            self.driver.find_element_by_xpath("//*[text()='账号和密码不匹配，请重新输入']")
            assert True
        except Exception:
            assert False
if __name__ == '__main__':
    unittest.main()
    suite = unittest.suite
    suite.addTest(Test_Log('test_Login_fail'))
    runer = unittest.TextTestRunner
    runer.run(suite)