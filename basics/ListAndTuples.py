"""
List is Mutable(changes can be done)
Tuples and Strings are immutable (data can't be changed)
"""

#List - Collection of data

fruits=["apple","pear","Orange"]

for fruit in fruits:
    print(fruit)

#List operations
fruits.append("strawberry")
print(fruits.count("apple"))
newFruits=["Grape","Mango"]
fruits.extend(newFruits)
fruits.remove("pear")
print(fruits.index("Grape"))


for fruit in fruits:
    print(fruit)

#Tuples - collection of immutable data

color =(255,252,251)

#Tuples Operations
print(color.count(255))
print(color.index(255))

#String

testString=" string "

#String Operators
print(testString.strip())
print(len(testString))
print(testString.capitalize())
print(testString.find("str"))
print(testString.count("s"))
print(testString) #string is not capitalized because it is immutable

#Slice operator
print(fruits[2]) # variable[start:stop:step]
print(testString[1:len(testString):2])
print(testString[2:]) #til end
print(testString[::3]) # skip every 3rd character
fruits[1:1]="b" #insert a character in the list
print(fruits)