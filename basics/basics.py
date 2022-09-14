#variables
name="sanjay"
age=float(21)

#data type check
print("data type check-----------------------------------------------")
print(isinstance(name,str))
print(isinstance(age,float))

#casting
print("Casting-----------------------------------------------")
num=20
float_num=float(num)
print(isinstance(num,int))
print(isinstance(float_num,float))

#ternary operator
def check_age(age):
    return True if age>18 else False

#Strings 
    #Immutables
print("Strings-----------------------------------------------")
print(name.lower())
print(name)

#slicing
print("Slicing-----------------------------------------------")
print(name[2:])
print(name[:3])
print(name[:-2])

#boolean
print("boolean-----------------------------------------------")
bool1=True
bool2=False
print(any([bool1,bool2])) #if any of the data is true
print(all([bool1,bool2])) #if all the data are true

#complex numbers, u can create it as num1 or num2 way
print("Complex numbers-----------------------------------------------")
num1=2+3j 
num2=complex(2,3)
print(num2.real,num2.imag)

#list are mutables
print("Lists-----------------------------------------------")
list1=["1","2","3","4"]
list1.remove("2")
print(list1)
list1.sort(key=str.lower)
list1.append("3")
list1=sorted(list1,key=str.lower) #sorting
print(list1)

#tuples are immutables
print("tuples-----------------------------------------------")
tuples=("1","2","3","1")
sorted(tuples,key=str.lower)#won't change the orginal data
print(tuples)

#sets
print("Sets-----------------------------------------------")
set1={"1","2","1"}
print(set1)
set2={"1"}
sub=set1 - set2 #subract and get unique values
print(sub)
mod=set1 | set2 #combine two sets
print(mod)

#functions
def counter():
    count=0
    def increment():
        nonlocal count #to access the declared count
        count=count+1
        return count
    return increment
increment=counter()

print(increment())

#loops

items=[1,2,4,5]
for index,item in enumerate(items):
    print(f"{item} at index {index}")

