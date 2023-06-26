"""
Types:
    For Loop
    While Loop
"""

#For Loop

for x in range(0,10,1): # start(from -0), stop(excluded- 10), step - 1
    print(x)

#While Loop
x=0
while(x<10): #Condition
    if(x==8):
        break #loop ends
    elif(x==5):
        x=x+1 #increment
        continue #skip
    print(x)   
    x=x+1 #increment