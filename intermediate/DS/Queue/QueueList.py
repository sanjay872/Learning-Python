class QueueList:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        if len(self.storage)>0:
            head=self.storage[0]
            if head:
                self.storage.append(new_element)
            else:
                self.storage[0]=new_element
        else:
            self.storage.append(new_element)
    
    def peek(self):
        return self.storage[0]

    def dequeue(self):
        head=None
        if len(self.storage)>0:
            head=self.storage[0]
            if head:
                self.storage=self.storage[1:]
        else:
            self.storage=[]
        return head
    
# Setup
q = QueueList(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())