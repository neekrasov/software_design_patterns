from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
        
class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")

# Модуль верхего уровня Research зависит от модуля нижнего уровня Relationships
# Изменив модуль нижнего уровня, придётся также изменять модуль верхнего уровня.