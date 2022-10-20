# Часто так бывает, что копии вручную делать не удобно.
# В это нам может помочь паттерн Фабрика.

from copy import copy


class Address:
    def __init__(self, street_address, city, suite) -> None:
        self.city = city
        self.street_address = street_address
        self.suite = suite

    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.suite}"


class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", "London", "0"))
    aux_office_employee = Employee("", Address("125 West Dr", "London", "0"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


if __name__ == "__main__":
    john = EmployeeFactory.new_main_office_employee("John", 101)
    jane = EmployeeFactory.new_aux_office_employee("Jane", 500)
    print(john)
    print(jane)
