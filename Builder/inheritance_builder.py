# Builder Through Inheritance
# Решает проблему исходного корневого строителя, который зависит от дочерних строителей
# Каждый строить открыт для расширения, но закрыт для модификации


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    @staticmethod
    def new():
        return PersonBuilder()

    def __str__(self) -> str:
        return f"Name: {self.name}, Position: {self.position}, Date of Birth: {self.date_of_birth}"


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    person = (
        PersonBirthDateBuilder()
        .called("John")
        .works_as_a("Engineer")
        .born("1990")
        .build()
    )
    print(person)
