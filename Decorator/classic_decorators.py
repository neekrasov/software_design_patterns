import abc

class Shape(abc.ABC):
    def __str__(self):
        return self.__class__.__name__
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def resize(self, factor):
        self.radius *= factor
        
    def __str__(self):
        return "{} with radius {}".format(self.__class__.__name__, self.radius)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def __str__(self):
        return "{} with side {}".format(self.__class__.__name__, self.side)

class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise TypeError("Cannot apply ColoredShape twice")
        self.shape = shape
        self.color = color
        
    def __str__(self):
        return "{} colored {}".format(self.shape, self.color)

class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        if isinstance(shape, TransparentShape):
            raise TypeError("Cannot apply TransparentShape twice")
        self.shape = shape
        self.transparency = transparency
        
    def __str__(self):
        return "{} with {}% transparency".format(self.shape, self.transparency*100)
    
if __name__ == "__main__":
    circle = Circle(5)
    print(circle)
    
    red_circle = ColoredShape(circle, "red")
    print(red_circle)
    
    red_square = ColoredShape(Square(5), "red")
    print(red_square)
    
    transparent_square = TransparentShape(Square(5), 0.5)
    print(transparent_square)
    
    red_transparent_square = ColoredShape(transparent_square, "red")
    print(red_transparent_square)