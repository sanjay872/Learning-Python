"""
Inheritance is passing of abilities of One Class to another.
"""

class Animal:
    
    def __init__(self,name) -> None:
        self.name=name
    
    def getName(self):
        return self.name

    def eat(self):
        print(self.name+" eats!")
    
    def walk(self):
        print(self.name+" walks!")

class Tiger(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def hunt(self):
        print(super().getName()+" Hunts!")

class Dog(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)
    
tiger=Tiger("Mack")
dog=Dog("Spoof")

print(tiger.eat())
print(tiger.hunt())
print(dog.walk())