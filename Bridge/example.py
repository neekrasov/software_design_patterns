# VectorCircle VectorSquare RasterCircle RasterSquare? No! This is not scalable!

import abc

# but render class violates the OCP :(
class Render(abc.ABC):
    def render_circle(self, radius):
        pass


class VectorRender(Render):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class RasterRender(Render):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:  # Core
    def __init__(self, render):
        self.render = render

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, render, radius):
        super().__init__(render)
        self.radius = radius

    def draw(self):
        self.render.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRender()
    vector = VectorRender()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle2 = Circle(raster, 5)
    circle2.draw()
    circle2.resize(2)
    circle2.draw()
