from sharpie import *
import unittest

obj = Sharpie("red", 1.5)

class FirstTest(unittest.TestCase):

    def test_default(self):
        self.assertEqual(obj.color,"red")
        self.assertEqual(obj.ink_amount,100)

    def test_not_default(self):
        obj=Sharpie('red',1.5,0)
        self.assertEqual(obj.ink_amount,0)

    def test_use(self):
        obj.use()
        self.assertEqual(obj.ink_amount,95)

if __name__ == '__main__':
    unittest.main()