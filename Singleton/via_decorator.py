# Одно из решений проблемы инициализации объектов. (предотвращает двойдой вызов __init__)


def singelton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singelton
class Database:
    def __init__(self) -> None:
        print("init called")


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
    print(id(db1) == id(db2))

    # Вывод:
    # init called
    # True
    # True
