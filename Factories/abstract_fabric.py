import abc
from enum import Enum, auto


class HotDrink(abc.ABC):
    @abc.abstractmethod
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("This tea is nice with lemon!")
    
class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious!")
        
class HotDrinkFactory(abc.ABC): # optional class in python
    @abc.abstractmethod
    def prepare(self, amount):
        pass
    
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, add lemon, enjoy!")
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, add cream and sugar, enjoy!")
        return Coffee()
    
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFEE = auto()
        TEA = auto()
    
    factories = []
    initialized = False
    
    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
                
    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])
        
        idx = int(input(f"Please pick drink (0-{len(self.factories)-1}): "))
        amount = int(input("Specify amount: "))
        return eval(self.factories[idx][0]).prepare(amount)

    
if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.make_drink()
    