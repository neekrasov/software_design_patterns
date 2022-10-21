import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.population = {}
        with open("Singleton/files/capitals.txt", "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = int(lines[i + 1].strip())


class SingletonRecordFinder:
    def __init__(self, db) -> None:
        # Dependency injection (Зависимость от абстракции)
        # При необходимости базу данных можно заменить на любую.
        # Тестирование от этого страдать не будет.

        # Пример: в библиотеке fastapi с помощью dependency_overrides
        # можно заменить неокторые зависимости для тестирования, и всё будет прекрасно работать.
        self.db = db

    def total_population(self, names):
        result = 0
        for name in names:
            result += self.db.population[name]
        return result


class DummyDatabase:
    def __init__(self) -> None:
        self.population = {
            "alpha": 1,
            "beta": 2,
            "gamma": 3,
        }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    ddb = DummyDatabase()

    def test_is_singleton(self):
        db = Database()
        db2 = Database()
        self.assertEqual(db, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder(self.ddb)
        tp = rf.total_population(["alpha", "gamma"])
        self.assertEqual(tp, 4)


if __name__ == "__main__":
    unittest.main()
