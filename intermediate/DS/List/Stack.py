class Element:

    def __init__(self,value=None):
        self.value=value
        self.next=None

class Stack:

    def __init__(self,head=None):
        self.head=head
        if self.head:
            self.length=1
        else:
            self.length=0
    
    def push(self,newElement):
        if self.head:
            newElement.next=self.head
            self.head=newElement
        else:
            self.head=newElement
        self.length+=1

    def pop(self):
        top=self.head
        if top:
            self.head=top.next
            top.next=None
            self.length-=1
        return top    
    
    def peek(self):
        top=self.head
        if self.head:
            return top.value
        return top

    def display(self):
        curElement=self.head
        if curElement:
            while curElement:
                print(curElement.value,end=" ")
                curElement=curElement.next
            print("",end="\n")
        else:
            print("Stack is Empty!")

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)

stack=Stack(e1) # in stack 1

stack.push(e2) # in stack 2 1 
stack.push(e3) # in stack 3 2 1
stack.push(e4) # in stack 4 3 2 1

stack.display() # displays 4 3 2 1

stack.pop() # in stack 3 2 1
stack.pop() # in stack 2 1

stack.display() # displays 2 1

print(stack.peek()) # returns 2

stack.display() # displays 2 1