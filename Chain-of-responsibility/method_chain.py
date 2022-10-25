class Creature:
    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add(self, modifier):
        if self.next_modifier:
            self.next_modifier.add(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1
        super().handle()

class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you!")

if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)


    # root.add(NoBonusesModifier(goblin))

    root.add(DoubleAttackModifier(goblin))
    root.add(IncreaseDefenseModifier(goblin))

    root.handle()
    print(goblin)
