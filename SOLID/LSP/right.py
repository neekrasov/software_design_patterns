class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    # Лучше будет сделать так, и не использовать наследование
    def is_square(self):
        return self._width == self._height

    @property
    def area(self):
        return self._width * self._height

    @property
    def height(self):
        return self._height

    @property.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @property.setter
    def width(self, value):
        self._width = value

    def __str__(self):
        return f"Rectangle with width {self._width} and height {self._height}"
