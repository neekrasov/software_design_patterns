import abc
from enum import Enum

# Product
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size


# Specification
class Specification(abc.ABC):
    @abc.abstractmethod
    def is_satisfied(self, item):
        raise NotImplementedError

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class OrSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return any(map(lambda spec: spec.is_satisfied(item), self.args))


# Filter
class Filter(abc.ABC):
    @abc.abstractmethod
    def filter(self, items, spec: Specification):
        raise NotImplementedError


class BetterFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    filter = BetterFilter()
    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in filter.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in filter.filter(products, large):
        print(f" - {p.name} is large")

    print("Large blue items:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in filter.filter(products, large_blue):
        print(f" - {p.name} is large and blue")

    print("Large or green items:")
    large_or_green = large | green
    for p in filter.filter(products, large_or_green):
        print(f" - {p.name} is large or green")

    large_and_green = large & green
    for p in filter.filter(products, large_and_green):
        print(f" - {p.name} is large and green")
