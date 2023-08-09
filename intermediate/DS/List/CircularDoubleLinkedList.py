class Element:
    def __init__(self,value):
        self.prev=None
        self.value=value
        self.next=None

class CircularDoubleLinkedList:
    def __init__(self,head=None):
        self.head=head
        self.tail=head
        self.head.next=self.tail
        if self.head:
            self.length=1
        else:
            self.length=0

    def append(self,newElement):
        if self.head:
            tail=self.tail
            tail.next=newElement
            newElement.prev=tail
            newElement.next=self.head
            self.tail=newElement
        else:
            self.head=newElement
            self.tail=newElement
            newElement.next=self.head
        self.length+=1
    
    def insert(self,newElement,pos):
        if self.head:
            if pos>=1 and pos<=self.length:
                head=self.head
                prevElement=head.prev
                curPos=1
                while head.next!=self.head and curPos<pos:
                    prevElement=head
                    head=head.next
                    curPos+=1
                if prevElement:
                    prevElement.next=newElement
                    newElement.prev=prevElement
                    newElement.next=head
                    head.prev=newElement
                else:
                    newElement.next=self.head
                    self.head.prev=newElement
                    self.head=newElement
                    self.tail.next=newElement
                    newElement.prev=self.tail
                self.length+=1
            else:
                print("Invalid Position!")
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
                        head.next.prev=prevElement
                    else:
                        prevElement.next=self.tail.next
                        self.head.prev=prevElement
                        self.tail=prevElement
                else:
                    self.head=head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
                head.prev=None
                head.next=None
                self.length-=1
            else:   
                print("Value not found")
        else:
            print("List is empty")

    def extend(self,cdl2):
        if self.head:
            if cdl2.head:
                self.tail.next=cdl2.head
                self.tail=cdl2.tail
                self.tail.next=self.head
                self.head.prev=self.tail
                self.length+=cdl2.size()
            else:
                print("No element in given list")    
        else:
            print("No element in current list")

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

    def size(self):
        return self.length
    
    def clean(self):
        self.head=None
        self.tail=None
        self.length=0

    def display(self):
        if self.head:
            head=self.head
            while head!=self.tail:
                print(head.value,end=" ")
                head=head.next
            print(head.value,end="\n")
        else:
            print("List is Empty")

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

cdl=CircularDoubleLinkedList(e1) # in list 1
cdl.append(e2) # in list 1 2
cdl.append(e3) # in list 1 2 3
cdl.append(e4) # in list 1 2 3 4
cdl.append(e5) # in list 1 2 3 4 5

cdl.display() # displays 1 2 3 4 5

print(cdl.size()) # length is 2

cdl.insert(e6,1) # changed to 6 1 2 3 4 5
cdl.insert(e7,3) # changed to 6 1 7 2 3 4 5
cdl.insert(e8,2) # changed to 6 8 1 7 2 3 4 5
cdl.insert(e9,7) # changed to 6 8 1 7 2 3 9 4 5

cdl.display() # displays 6 8 1 7 2 3 9 4 5

# cdl.clean()
# cdl.insert(e1,2) # List is Empty

cdl.delete(6) # changed to 8 1 7 2 3 9 4 5
cdl.delete(7) # changed to 8 1 2 3 9 4 5
cdl.delete(5) # changed to 8 1 2 3 9 4
cdl.delete(11) # Value not found

print(cdl.size()) # prints 6

cdl.display() # display 8 1 2 3 9 4

cdl2=CircularDoubleLinkedList(Element(11))
cdl2.append(Element(21))

cdl.extend(cdl2)
print(cdl.size()) # prints 8
cdl.display() # displays 8 1 2 3 9 4 11 21

print(cdl.get_position(8)) # returns 1
print(cdl.get_position(2)) # returns 3
print(cdl.get_position(21)) # returns 8
print(cdl.get_position(5)) # returns None

cdl.update(1,0) # changed to 8 1 2 3 9 4 11 21
cdl.update(5,4) # changed to 0 1 2 3 4 4 11 21
cdl.update(6,5) # changed to 0 1 2 3 4 5 11 21
cdl.update(8,12) # changed to 0 1 2 3 4 5 11 21
cdl.update(9,12) # invalid Position

cdl.display() # displays 0 1 2 3 4 5 11 12