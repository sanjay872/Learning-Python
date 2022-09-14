import dog #import a file
from dog import walk #import a function

from lib import cat #import from different folder
from lib.cat import meow #import from different folder specific function

#inbuild modules
import math

dog.walk()
walk()

cat.meow()
meow()

print(math.sqrt(4))