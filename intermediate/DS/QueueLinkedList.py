class Element:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class QueueLinkedList:
    def __init__(self,head=None):
        self.head=head
        self.tail=head
        if self.head:
            self.length=1
        else:
            self.length=0
    
    def enqueue(self,newElement:Element):
        if self.head:
            self.tail.next=newElement
            self.tail=newElement
        else:
            self.head=newElement

    def dequeue(self):
        curElement=self.head
        if curElement:
            self.head=curElement.next
        return curElement
    
    def peek(self):
        return self.head
    
    def display(self):
        head=self.head
        tail=self.tail
        if head:
            if tail:
                while head:
                    print(head.value,end=" ")
                    head=head.next
                print("",end="\n")
            else:
                print(head.value)
        else:
            print("No Elements")

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)

q=QueueLinkedList(e1) # In queue 1 

q.enqueue(e2) # In queue 1 2
q.enqueue(e3) # In queue 1 2 3
q.enqueue(e4) # In queue 1 2 3 4
q.enqueue(e5) # In queue 1 2 3 4 5

q.display()# displays 1 2 3 4 5

q.dequeue() # In queue 2 3 4 5
q.dequeue() # In queue 3 4 5
q.dequeue() # In queue 4 5
q.dequeue() # In queue 5
#q.dequeue() # In queue 

print(q.peek().value) # returns 5

q.display() # displays 5