# Factory Method Pattern

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))


if __name__ == "__main__":
    p = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(1, math.pi / 2)
