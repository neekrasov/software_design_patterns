# Моносостояние это вариация одиночки при котором состояние объекта хранится в статическом поле класса.
# Клиент может создавать новые экземпляры класса, но все они будут иметь одно и то же состояние.


class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 50,
    }

    def __init__(self) -> None:
        # Фишка в том, что при каждой инициализации экземпляра класса
        # мы перезаписываем __dict__ экземпляра класса на __shared_state,
        # то есть словарь атрибутов един для всех инстансов (экземпляров класса).
        # Копируем ссылку на словь атрибутов со всеми значениями.
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 100
    print(ceo2)

    print(ceo1)
    print(ceo1 == ceo2)

    # Вывод:
    # Steve is 50 years old
    # Steve is 100 years old
    # Steve is 100 years old
    # True
