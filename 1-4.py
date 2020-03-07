from selenium import webdriver
import unittest
class JD(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_1397b6c04eed4a6fb097d0d955dd061f')
        self.driver.implicitly_wait(3)
    def tearDown(self):
        self.driver.quit()
    def test_jd(self):
        self.driver.find_element_by_id('key').send_keys('10086')
        self.driver.find_element_by_class_name('button').click()
        try:
            self.driver.find_element_by_xpath('//*[text()="10086"]')
            assert True
        except Exception:
            assert False
if __name__ == '__main__':
    unittest.main()