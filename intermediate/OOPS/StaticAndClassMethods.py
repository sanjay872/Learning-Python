"""
Static Methods are independent of the class
    - self or any other instance of the class can't be used in it.
Class Methods are depend on the class
"""

class Dog:
    dogs=[]

    def __init__(self,name) -> None:
        self.name=name
        self.dogs.append(self)
    
    @classmethod
    def num_dogs(cls): # arg is this class
        return len(cls.dogs)
    
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("Bark:")

#Class methods
print(Dog.num_dogs())
dog1= Dog("dog1")
print(Dog.num_dogs())
dog2= Dog("dog2")
print(dog2.num_dogs())

#static methods
Dog.bark(10)

class Math:
    @staticmethod
    def add(x,y):
        return x+y
    
print(Math.add(1,2))