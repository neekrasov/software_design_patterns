class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f"A doctor has been called to {address} for {name}")


if __name__ == "__main__":
    # however this method is very difficult to scale
    person = Person("John", "123 London Road")
    person.falls_ill.append(call_doctor)
    person.catch_cold()
    person.falls_ill.remove(call_doctor)
