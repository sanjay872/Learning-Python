class StackList:
    
    def __init__(self,value) -> None:
        if value:
            self.stack=[value]
            self.length=1
        else:
            self.stack=[]
            self.length=0
    
    def push(self,value):
        self.stack.append(value)
        self.length+=1

    def pop(self):
        stack=self.stack
        size=self.length
        if size>=1:
            self.stack=stack[0:size]
            self.length-=1
        else:
            print("Stack is empty")
    
    def peek(self):
        if len(self.stack)>0:
            return self.stack[0]
        return None

    def display(self):
        i=self.length-1
        while i>=0:
            print(self.stack[i],end=" ")
            i-=1
        print(" ",end="\n")

s=StackList(1) # in stack 1
s.push(2) # in stack 2 1
s.push(3) # in stack 3 2 1
s.push(4) # in stack 4 3 2 1
s.push(5) # in stack 5 4 3 2 1

s.display() # displays 5 4 3 2 1

s.pop() # in stack 4 3 2 1
s.pop() # in stack 3 2 1
s.pop() # in stack 2 1
s.pop() # in stack 1
#s.pop() # in stack 
#s.pop() # stack is empty

print(s.peek()) # returns 1

s.display() # displays 1
