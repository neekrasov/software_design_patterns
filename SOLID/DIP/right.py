import abc
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name
        
class RelationshipBrowser(abc.ABC):
    # Если нужно будет изменить реализацию отношений, достаточно будет переопределить данный метод.
    # Не придётся изменять модуль верхнего уровня.
    @abc.abstractclassmethod
    def find_all_children_of(self, name):
        raise NotImplementedError
    
class Relationships(RelationshipBrowser): # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
        
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name
                
class Research: # high-level
    def __init__(self, browser: RelationshipBrowser , name: str):
        for p in browser.find_all_children_of(name):
            print(f"{name.capitalize()} has a child called {p}")