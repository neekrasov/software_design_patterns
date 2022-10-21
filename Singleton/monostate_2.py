# Вторая вариация с наследованием.


class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs) -> bool:
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CEO(Monostate):
    def __init__(self) -> None:
        self.name = "Steve"
        self.age = 50

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


if __name__ == "__main__":
    ceo1 = CEO()
    ceo1.age = 100
    print(ceo1)

    ceo2 = CEO()
    ceo2.name = "Tim"

    print(ceo1)
    print(ceo2)
