# Метакласс позволяет создавать объект класса.
# Реализация схожа с декоратором.


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print("init called")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
