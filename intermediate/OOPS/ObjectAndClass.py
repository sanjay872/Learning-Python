"""
Object is a created from a blueprint know as Class
All the initialised variables are objects
"""
# X="String"
# print(type(X)) # type is String object
# X.capitalize() # Capitalize is the function defined within that Object Class


# import turtle

# t=turtle.Turtle()

# print(t.circle(30))


"""
Class is the blueprint of object, it has functions
"""

class myclass:

    def __init__(self,name) -> None: #constructor
        self.name=name #self.name is local variable
    
    def getName(self) -> str: #getter
        return self.name

testClass=myclass("Sanjay")
print(testClass.name)