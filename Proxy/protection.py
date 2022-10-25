class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)
    
    def drive(self):
        if self.driver.age >= 18:
            self._car.drive()
        else:
            print("Driver too young")

class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print('Car is being driven by {}'.format(self.driver.name))


if __name__ == '__main__':
    driver = Driver('John', 18)
    car = CarProxy(driver)