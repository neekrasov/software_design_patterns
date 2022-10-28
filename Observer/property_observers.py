class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropetryObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropetryObservable):
    def __init__(self, age):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Not old enough to drive")
            else:
                print("Old enough to drive")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":
    p = Person(10)
    ta = TrafficAuthority(p)
    for age in range(11, 20):
        print(f"Setting age to {age}")
        p.age = age
