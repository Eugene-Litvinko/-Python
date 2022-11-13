import unittest
import math
from HT_5_class import Round, Quadrate, Rectangle, Triangle

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle()
        self.b = Round()
        self.c = Quadrate()
        self.d = Triangle()

    def test_rectangle(self):
        self.assertEqual(self.a.square(10, 20), float(10 * 20))
        self.assertEqual(self.a.square(4, 8), float(4 * 8))

    def test_round(self):
        self.assertEqual(self.b.square(4), float(math.pi * 4 ** 2))

    def test_quadrate(self):
        self.assertEqual(self.c.square(4), float(4 ** 2))

    def test_triangle(self):
        self.assertEqual(self.d.square(6, 8, 10), float(24))

if __name__ == "__main__":
    unittest.main()
