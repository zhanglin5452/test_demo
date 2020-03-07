import unittest
from selenium import webdriver
from time import sleep
class kkk(unittest.TestCase):
    def test_lll(self):
        print('1')
    def test_mmm(self):
        print('2')
    def test_jjj(self):
        print('3')
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(kkk('test_lll'))
    suite.addTest(kkk('test_jjj'))
    runer = unittest.TextTestRunner()
    runer.run(suite)