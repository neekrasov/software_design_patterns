class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class DatabaseWrong:
    _instance = None

    def __init__(self) -> None:
        print("init called")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
    print(id(db1) == id(db2))

    # При объявлении __init__ конструкция к сожалению ломается.
    # Т.к __init__ вызывается при каждом создании экземпляра класса после __new__
    # Да, мы получаем ссылку на один и тот же объект, однако
    # Инициализация экземпляра класса происходит повсеместно
    db1_1 = DatabaseWrong()
    db1_2 = DatabaseWrong()
    print(db1_1 == db1_2)
    print(id(db1_1) == id(db1_2))

    # Вывод:
    # True
    # True
    # init called
    # init called
    # True
    # True
