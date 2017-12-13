from animal import *
import unittest

obj = Animal("lion", 10,10)

class FirstTest(unittest.TestCase):

    def test_not_default(self):
        self.assertEqual(obj.name,"lion")
        self.assertEqual(obj.hunger,10)
        self.assertEqual(obj.thirst,10)

    def test_default(self):
        obj = Animal("lion")
        self.assertEqual(obj.name,"lion")
        self.assertEqual(obj.hunger,50)
        self.assertEqual(obj.thirst,50)

    def test_eat(self):
        obj_b = Animal('rat')
        obj_b.eat()
        self.assertEqual(obj_b.hunger,49)

    def test_drink(self):
        obj_c = Animal('carrot')
        obj_c.drink()
        self.assertEqual(obj_c.thirst,49)

    def test_play(self):
        obj_d = Animal('badcat')
        obj_d.play()
        self.assertEqual(obj_d.hunger,51)
        self.assertEqual(obj_d.thirst,51)

if __name__ == '__main__':
    unittest.main()