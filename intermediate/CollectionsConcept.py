"""
Collections are containers to store data
Types -List, Set, Dict, Tuple, 
        counter, Deque, namedTuple, orderedDict, defautdict
"""

# list and Tuple are in basic

# Set 


# Dict 


#Counter accepts any collection type data
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


#Deque

#NamedTuple