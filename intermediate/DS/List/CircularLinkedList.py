class Element:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self,head=None):
        self.head=head
        self.tail=head
        self.tail.next=self.head
        if self.head:
            self.length=1
        else:
            self.length=0

    def append(self,newElement):
        if self.head:
            tail=self.tail
            while tail.next!=self.head:
                tail=tail.next
            tail.next=newElement
            self.tail=newElement
            self.tail.next=self.head
        else:
            self.head=newElement
            self.tail=newElement
            self.tail.next=self.head
        self.length+=1
    
    def insert(self,newElement,pos):
        if self.head:
            if pos>=1 and pos<=self.length:
                head=self.head
                prevElement=None
                curPos=1
                while curPos<pos:
                    prevElement=head
                    head=head.next
                    curPos+=1
                if prevElement:
                    prevElement.next=newElement
                    newElement.next=head
                else:
                    self.head=newElement
                    newElement.next=head
                    self.tail.next=self.head
                self.length+=1
            else:
                print("Invalid position!")
        else:
            print("List is Empty")

    def delete(self,value):
        if self.head:
            head=self.head
            prevElement=None
            while head.next!=self.head and head.value!=value:
                prevElement=head
                head=head.next
            if head.value==value:
                if prevElement:
                    if head!=self.tail:
                        prevElement.next=head.next
                        head.next=None
                    else:
                        prevElement.next=self.tail.next
                        self.tail.next=None
                        self.tail=prevElement
                else:
                    self.tail.next=self.head.next
                    self.head.next=None
                    self.head=self.tail.next
                self.length-=1
            else:
                print("Value Not found!")
        else:
            print("List is empty!")

    def get_position(self,value):
        if self.head:
            head=self.head
            curPos=1
            while head.next!=self.head and head.value!=value:
                head=head.next
                curPos+=1
            if head.value==value:
                return curPos
            return None
        else:
            print("List is Empty")

    def extend(self,cl2):
        if self.head:
            if cl2.head:
                self.tail.next=cl2.head
                self.tail=cl2.tail
                self.tail.next=self.head
                self.length+=cl2.size()
            else:
                print("No element in given list")    
        else:
            print("No element in current list")

    def update(self,pos,newValue):
        if self.head:
            if pos>=1 and pos <= self.length:
                head=self.head
                curPos=1
                while head.next!=self.head and curPos<pos:
                    head=head.next
                    curPos+=1
                head.value=newValue
            else:
                print("Invalid Position!")
        else:
            print("List is Empty")

    def clean(self):
        self.head=None
        self.tail=None
        self.length=0

    def size(self):
        return self.length

    def display(self):
        if self.head:
            head=self.head
            while head!=self.tail:
                print(head.value,end=" ")
                head=head.next
            print(head.value,end="\n")
        else:
            print("No Elements!")

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)
e6=Element(6)
e7=Element(7)
e8=Element(8)
e9=Element(9)
e10=Element(10)

cl=CircularLinkedList(e1) # in list 1
cl.append(e2) # in list 1 2
cl.append(e3) # in list 1 2 3
cl.append(e4) # in list 1 2 3 4
cl.append(e5) # in list 1 2 3 4 5

cl.display() # displays 1 2 3 4 5

print(cl.size()) # length is 2

cl.insert(e6,1) # changed to 6 1 2 3 4 5
cl.insert(e7,3) # changed to 6 1 7 2 3 4 5
cl.insert(e8,2) # changed to 6 8 1 7 2 3 4 5
cl.insert(e9,7) # changed to 6 8 1 7 2 3 9 4 5

cl.display() # displays 6 8 1 7 2 3 9 4 5

#cl.clean()
#cl.insert(e1,2) # List is Empty

cl.delete(6) # changed to 8 1 7 2 3 9 4 5
cl.delete(7) # changed to 8 1 2 3 9 4 5
cl.delete(5) # changed to 8 1 2 3 9 4
cl.delete(11) # Value not found

print(cl.size()) # prints 6

cl.display() # display 8 1 2 3 9 4

cl2=CircularLinkedList(Element(11))
cl2.append(Element(21))

cl.extend(cl2)
print(cl.size()) # prints 8
cl.display() # displays 8 1 2 3 9 4 11 21

print(cl.get_position(8)) # returns 1
print(cl.get_position(2)) # returns 3
print(cl.get_position(21)) # returns 8
print(cl.get_position(5)) # returns None

cl.update(1,0) # changed to 8 1 2 3 9 4 11 21
cl.update(5,4) # changed to 0 1 2 3 4 4 11 21
cl.update(6,5) # changed to 0 1 2 3 4 5 11 21
cl.update(8,12) # changed to 0 1 2 3 4 5 11 21
cl.update(9,12) # invalid Position

cl.display() # displays 0 1 2 3 4 5 11 12