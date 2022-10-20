from copy import copy
import copyreg


class Address:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country
    
    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"

if __name__ == "__main__":
    # Jane реплицирует и изменяет части John, что легче чем инициализировать объект с нуля
    john = Person('John', Address('123 London Road', 'London', 'UK'))
    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street_address = '124 London Road'
    print(john)
    print(jane)