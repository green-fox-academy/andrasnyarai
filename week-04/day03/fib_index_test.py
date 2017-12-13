from fib_index import *
import unittest

class FirstTest(unittest.TestCase):

    def test_if_valid(self):
        self.assertEqual(fibonacci(4),3)

    def test_if_string(self):
        self.assertEqual(fibonacci("n"),"n")

    def test_if_float(self):
        self.assertEqual(fibonacci(2.5),2.5)

    def test_if_operator(self):
        self.assertEqual(fibonacci(2+2),3)

    def test_if_bool(self):
        self.assertEqual(fibonacci(True),True)

if __name__ == '__main__':
    unittest.main()