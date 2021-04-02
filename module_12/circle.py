# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 12 Practice 3
#
# Circle class with area and distance methods
# -----------------------------------------------------------------------------
from math import pi

class Circle:

    def __init__(self, x, y, radius):
        if (isinstance(x, (int, float)) and isinstance(y, (int, float)) and
            isinstance(radius, (int, float))):
            self.center = (x, y)
            self.radius = radius
        else:
            raise TypeError

    def get_area(self):
        area = pi * self.radius ** 2
        return area

    def get_distance(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            square_diff_x = (self.center[0] - x) ** 2
            square_diff_y = (self.center[1] - y) ** 2
        else:
            raise TypeError
        distance = (square_diff_x + square_diff_y) ** 0.5
        return distance


def main():
    circle = Circle(1, 1, 3)
    print(circle.get_area())
    print(circle.get_distance(1, 3))


main()