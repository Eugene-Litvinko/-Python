import math

class Shape:

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        # if self.a == 0:
        #     self.a = Shape.area()
        # if self.b == 0:
        #     self.b = Shape.area()
        # if self.c == 0:
        #     self.c = Shape.area()

    @staticmethod
    def area():
        print('Невозможно посчитать')

class Round(Shape):
    # def __init__(self):
    #     super(Round, self).__init__(a)

    def square(self, a):
        square = math.pi * float(a) ** 2
        return square

class Quadrate:

    def square(self, a):
        square = a ** 2
        return square

class Triangle(Shape):

    def square(self, a, b, c):
        p = (a + b + c) / 2
        square = p * (p - a) * (p - b) * (p - c)
        return square

class Rectangle(Shape):

    def square(self, a, b):
        square = (a * b)
        return square

def test_square_rectangle():
    x = Rectangle()
    assert x.square(4, 5) == float(4 * 5)

def test_square_round():
    x = Round()
    assert x.square(4) == float(math.pi * 4 ** 2)

if __name__ == '__main__':
    shape_1 = Round()
    print(shape_1.square(4))
    shape_2 = Rectangle()
    print(shape_2.square(4, 5))