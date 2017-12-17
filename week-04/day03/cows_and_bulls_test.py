from cows_and_bulls import *
import unittest


class InputTesting(unittest.TestCase):

    def test_if_its_working(self):
        self.assertEqual(len(obj.generate()),4)

    def test_if_object(self):
        self.assertTrue(obj.playing)
        self.assertEqual(obj.counter, 0)
        self.assertEqual(len(str(obj.secret)),4)
        self.assertTrue(isinstance(obj.secret, str))

    def test_cab_counter_with_0000(self):
        obj.guess = '1111'
        obj.secret = '0000'
        obj.cab_counter()
        self.assertEqual(obj.cab_state, {'C' : 0, 'B' : 0})

    def test_cab_counter_with_1000(self):
        obj.guess = '1111'
        obj.secret = '1000'
        obj.cab_counter()
        self.assertEqual(obj.cab_state, {'C' : 1, 'B' : 3})


if __name__ == '__main__':
    unittest.main()