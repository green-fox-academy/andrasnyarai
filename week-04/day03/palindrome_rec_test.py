import palindrome_rec
import unittest

class FirstTest(unittest.TestCase):

    def test_check_if_palindrome_or_not(self):
        self.assertTrue(palindrome_rec.palindrome_check("kerek"))


if __name__ == '__main__':
    unittest.main()