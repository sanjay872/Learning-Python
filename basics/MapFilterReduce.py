from functools import reduce


numbers = [1,2,3,4,5,6,7]

#Map---------------------------------------------------->

def double(a):
    return a*2

#map converts data
print(list(map(double,numbers)))

#Filter-------------------------------------------------->

def even(num):
    return True if num%2==0 else False 

#filters data based on given condtion
print(list(filter(even,numbers)))

#reduce------------------------------------------------>

#example of calculating expenses
expenses=[
    ('movie',200),
    ('dinner',500)
]
sum=0
for expense in expenses:
    sum+=expense[1]
print(sum)

#doing the same using reduce

def calcuateExpenses(a,b): #a[1] has 0 as intital value for expense[1]  and b[1] is the values in list that gets iterated 
    return a[1]+b[1]

lambdaExpenses=lambda a,b: a[1] + b[1]

expenseSum=reduce(calcuateExpenses,expenses)
print(expenseSum)