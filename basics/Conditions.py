"""
Conditions
    Compare Operators: >, <, ==, !=, >=, <=
    Condition Operators: and(&), or(||), not(!), in(exist in a list)
"""
print(2>3, 2+3>3, 2==1)

# General Statements

age=int(input("Enter ur age!: "))

if(age>18):
    print("Eligible to vote!")
elif(age==18):
    print("First time voter!")
else:
    print("Not eligible to vote!")

# Ternary condtion

print("Eligible to Vote!" if age>18 else "Not eligible!" if age<18 else "First time voter!")

# multiple conditions
x=10
y=20
if(x>5 and y<30 and (x+y==30 or not(x<10) )):
    print("It is true")

#nested statements
    if(x>5 and y<30):
        if(x+y==30 or not(x<10)):
            print("it is true")
        else:
            print("Half true")
    else:
        print("Not true")
