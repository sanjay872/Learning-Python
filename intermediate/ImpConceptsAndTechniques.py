"""
Map is to convert data to different form
Filter is to remove or eliminate data
List Comprehension is short hand of map
Lambda is shorthand to define function
"""

#Map

l=[1,2,3,4,5,6]

def sqr(n):
    return n*2

print(list(map(sqr,l))) #parameter are function and data returns map object so, using list() to convert

#List Comprehensions

print([sqr(n) for n in l]) # function and the loop

#Filter

def isOdd(n):
    return n%2!=0

print(list(filter(isOdd,l)))

#Map and Filter

print(list(map(sqr,filter(isOdd,l))))

#Lambda

def add(x,y):
    return x+y

addV2= lambda x,y: x+y # lambda args: operation

print(add(1,2),addV2(1,2))

#Filter and lambda

print(list(filter(lambda x:x%2!=0,l)))