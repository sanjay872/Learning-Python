"""
Collections are containers to store data
Types -List, Set, Dict, Tuple, 
        counter, Deque, namedTuple, orderedDict, defautdict
"""

# list and Tuple are in basic

# Set - an unordered collection of unique elements

print("---------------------------------Start Set-------------------------------------------")

s=set([1,2,3,4]) #init
print(s)

s.add("a") # add data
print(s)

fs=frozenset([1,2,3,4])
print(fs) # this set is immutable so, no direct operations

s1=set([1,2,4,5])
s2=set([7,2,1,5])

print(s1.union(s2)) # combines all the values and removes duplicates
print(s1.difference(s2)) # removes all the elements in s1 that are found in s2

print(s1==s2)
print(s1>s2) #checks which set has most greater values
print(1 in s1) # return whether 1 exist in s1
print(s1^s2) #returns all unique values

print("---------------------------------End Set-------------------------------------------")

# Dict - unordered data stored as a pair of key and value
print("---------------------------------Start Dict-------------------------------------------")
d1={} #init
d1={1:"apple",2:"mango",3:"orange"}
d2=dict({1:"apple",2:"mango",3:"orange"})
d3=dict([(1,"apple"),(2,"mango"),(3,"orange")])
print(d1,d2,d3) #all are same, but different ways

d4={1:{"a":"A"},2:{"b":"B"}} #nested dictionaries

d1[1]="pear" #update value
print(d1)

d1[4]="mango" # add value
print(d1)

d1[4]={5:"strawberry"} # replace value with a dict
print(d1)

print(d4[1]["a"]) #accessing data
print(d4.get(1).get("a")) #another way of accessing

d2.pop(2) # delete item by passing key
print(d2)
d2.popitem() # removes the last element
print(d2)

print(d2.values()) #returns all values
keys={"a","b","c","d"}
value=1 #this value is same for all the keys
print(dict.fromkeys(keys,value)) #adds keys and values in unorder

d2.clear() #removes all the elements
print(d2) # returns {}

print("---------------------------------End Dict-------------------------------------------")

#Counter accepts any collection type data

print("---------------------------------Start Counter-------------------------------------------")
from collections import Counter

c= Counter("test")
c= Counter(["a","b"])
c = Counter({"a":1,"b":2})
print(c['a']) # to access a value


c= Counter(("a","b","b","a","c","a"))
print(c.most_common(2)) # arg- number of values we want, returns value and count

c=Counter(a=1,b=2,c=3)
d={'a':1,"b":3,"c":3}
c.subtract(d) # c - d subract counter with non counter object
print(c)
c.update(d) # c + d add counter with non counter object
print(c) # back to old values

d=Counter(["a","b","c","a"])
print(c+d) # addition
print(c-d) # sub
print(c & d) # intersection - get each min element
print(c | d) # union - get each max element 


print("---------------------------------End Counter-------------------------------------------")

#Deque - similar to list but faster in adding element. Accessing element is slow, List in prefered in this case.

print("---------------------------------Start Deque-------------------------------------------")

from collections import deque

d = deque("welcome")
print(d) #deque splits string into list of characters

d.append("!") # add
print(d)
d.pop() # removes last element
print(d)
d.appendleft("!") # add at beginning
print(d)
d.popleft() #remove at beginning
print(d)
d.extend("home") #adds all to the end
print(d)
d.extend([1,2,4]) # list of either character or number can be added easily at the end
print(d)
d.extendleft([5,6,7]) # list of either character or number can be added easily at the beginning
print(d)

#all the data appended from left will be in reverse order, because it is the way in which the give list is iterated
#EXAMPLE: to extend 5,6,7 the list must be read from 5 and 5 is the first element added from left. so it will be reverse order of the list.

d.rotate(2) # n =2, so it get 2 element from end and append it to the beginning
d.reverse() # completely reverses the order so, deque.rotate(deque.length) == deque.reverse()

d2=deque("Welcome",maxlen=7) # if 11 element is added, the first element will be removed and other elements postions are swapped to give space for 11th element
print(d2)
d2.append("!")
print(d2) # w is removed
print(d2.maxlen) # returns max lenght

print("---------------------------------End Deque-------------------------------------------")

#NamedTuple - same as regular tuple but, can be accessed by name


print("---------------------------------Start Named Tuple-------------------------------------------")

from collections import namedtuple

point=namedtuple('point','x y z') # tuple name, labels

newPt=point(3,4,5) #x=3, y=4, z=5
print(newPt)
print(newPt.x,newPt.y,newPt.z) # accessing each tuple by label

newPt1=newPt._replace(y=6)

print(newPt1.x,newPt1.y,newPt1.z) # value got replaced


print("---------------------------------End Named Tuple-------------------------------------------")