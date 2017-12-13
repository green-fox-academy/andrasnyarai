from andras_work import Apple, Summing
import unittest



apple_obj = Apple()

sum_obj = Summing()

class FirstTest(unittest.TestCase):

    def test_apple2(self):
        self.assertEqual(apple_obj.get_apple1("a"), "apple")

    def test_apple1(self):
        self.assertEqual(apple_obj.get_apple(), "apple")

class SecondTest(unittest.TestCase):

    def test_if_sum_empty_list(self):
        self.assertEqual(sum_obj.sum_of_num([]),0)

    def test_if_sum_is_equal_to_parts(self):
        self.assertEqual(sum_obj.sum_of_num([1,2,3]),6)

    def test_if_sum_one_element(self):
        self.assertEqual(sum_obj.sum_of_num([1]),1)

    def test_with_null(self):
        self.assertEqual(sum_obj.sum_of_num(),0)

if __name__ == '__main__':
    unittest.main()