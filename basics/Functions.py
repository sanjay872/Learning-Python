"""
Function holds instructions
"""

def addTwoNumbers(num1,num2):
    return num1+num2

print(addTwoNumbers(1,2))

#Recursion - function calls itself

def sumOfNumbers(n):
    if(n>=1):
        return n+sumOfNumbers(n-1)
    else:
        return n

print(sumOfNumbers(10))

#Optional parameters

def fun(x,y=10): # y is optional
    return x+y

print(fun(5))