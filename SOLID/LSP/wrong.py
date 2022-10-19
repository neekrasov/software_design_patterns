class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

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


class Square(Rectangle):
    # Нарушение LSP, квардат - частный случай прямоугольника, и он не нуждается в отдельной сущности,
    # поэтому мы не можем использовать метод базового типа в его подтипе (квадрате).
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @super().width.setter
    def width(self, value):
        self._width = self._height = value

    @super().height.setter
    def height(self, value):
        self._width = self._height = value
