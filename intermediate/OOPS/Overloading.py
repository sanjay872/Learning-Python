"""
To overwrite a exist function
Refer documents for other inbuild functions
"""
import math

class Point:

    def __init__(self,pt1=0,pt2=0) -> None:
        self.pt1=pt1
        self.pt2=pt2
    
    def move(self,pt1,pt2):
        self.pt1+=pt1
        self.pt2+=pt2
    
    def __add__(self,p): # on add self is p1 and p is p2
        return Point(self.pt1+p.pt1,self.pt2+p.pt2)

    def __sub__(self,p): # on sub self is p1 and p is p2
        return Point(self.pt1-p.pt1,self.pt2-p.pt2)
    
    def __mul__(self,p): # on mul self is p3 and p is p4
        return Point(self.pt1*p.pt1,self.pt2*p.pt2)
    
    def length(self): # to get length of a point
        return math.sqrt(self.pt1**2+self.pt2**2)

    def __gt__(self,p): # greater than comparison
        return self.length()>p.length()
    
    def __ge__(self,p): # greater than and equal comparison
        return self.length()>=p.length()
    
    def __eq__(self,p): # equal comparison
        return self.pt1==p.pt2 and self.pt2==p.pt2
    
    def __lt__(self,p): # less than comparison
        return self.length()<p.length()
    
    def __le__(self,p): # less than and equal comparison
        return self.length()<=p.length()

    def __str__(self): # on print this will executed
        return "("+str(self.pt1)+","+str(self.pt2)+")"

p1=Point(1,3)
p2=Point(2,3)
p3=p1+p2
p4=p1-p2
p5=p3*p4

print(p3)
print(p4)
print(p5)

print(p1==p2)
print(p1>p2)