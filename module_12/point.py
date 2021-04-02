# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 12 Practice 2
#
# Point class with distance method.
# -----------------------------------------------------------------------------
class Point:

    def __init__(self, x, y, z):
        if (isinstance(x, (int, float)) and isinstance(y, (int, float)) and
            isinstance(z, (int, float))):
            self.x = x
            self.y = y 
            self.z = z 
        else:
            raise TypeError
    
    def get_distance(self, origin=None):
        if origin == None:
            square_diff_x = self.x ** 2
            square_diff_y = self.y ** 2
            square_diff_z = self.z ** 2
        elif isinstance(origin, Point):
            square_diff_x = (self.x - origin.x) ** 2
            square_diff_y = (self.y - origin.y) ** 2
            square_diff_z = (self.z - origin.z) ** 2
        else:
            raise TypeError
        distance = (square_diff_x + square_diff_y + square_diff_z) ** 0.5
        return distance


def main():

    start = Point(1, 1, 1)
    print(start.get_distance())
    end = Point(1, 1, 2)
    print(start.get_distance(origin=end))


main()