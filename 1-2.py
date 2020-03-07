import unittest
class TestLogin(unittest.TestCase):
    def setUp(self):
        print('每个程序的起点')
    def tearDown(self):
        print('每个程序的终点')
    def test1(self):
        print('1')
    def test2(self):
        print('2')
    def test3(self):
        print('3')
if __name__ == '__main__':
    unittest.main()