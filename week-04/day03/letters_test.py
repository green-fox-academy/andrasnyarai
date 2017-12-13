from letters import *
import unittest

class FirstTest(unittest.TestCase):

    def test_count_occur(self):
        self.assertEqual(one_string("rrr"),{'r':3})

    def test_count_multiple(self):
        self.assertEqual(one_string("re"),{'r': 1, 'e': 1})

    def test_if_capital(self):
        self.assertEqual(one_string('Rr'),{'R': 1,'r': 1})

    def test_check_whitespace(self):
        self.assertEqual(one_string('  '),{' ': 2})

    def test_none(self):
        self.assertEqual(one_string(),{})

    def test_if_num(self):
        self.assertEqual(one_string(0),{'0' : 1})

if __name__ == '__main__':
    unittest.main()