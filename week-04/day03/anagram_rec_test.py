from anagram_rec import *
import unittest

class FirstTest(unittest.TestCase):

    def test_check_if_anagram_or_not(self):
        self.assertTrue(anagram_check("keret","teker"))

    def test_white_space(self):
        self.assertTrue(anagram_check("keret","t eker"))

    def test_capital(self):
        self.assertTrue(anagram_check("keret","T eker"))

if __name__ == '__main__':
    unittest.main()