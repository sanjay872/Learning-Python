class Animals:
    def walk(self):
        print("Walking!")

class Dog(Animals):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"woof!, I am {self.name} and my age is {self.age}")

mydog=Dog("PUP",4)
mydog.bark()
mydog.walk()