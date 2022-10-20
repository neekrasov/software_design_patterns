import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)
        
        def new_polar_point(self, rho, theta):
            return Point(rho * math.cos(theta), rho * math.sin(theta))
        
    factory = PointFactory()
    
if __name__ == "__main__":
    p = Point.factory.new_cartesian_point(2, 3)
    p2 = Point.factory.new_polar_point(1, math.pi / 2)