import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('#' * 30)
        print('Run once before all test')
        print('#' * 30)

    def setUp(self):
        print("Run before every test")

    def test_methodA(self):
        print("Running test method A")

    def test_methodB(self):
        print("Running test method B")

    def tearDown(self):
        print("Run after every test")

    @classmethod
    def tearDownClass(cls):
        print('#' * 30)
        print('Class 1 --> Class Level tearDown')
        print('#' * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
