fileName="./sample.txt"

try:
    file=open(fileName,'r')
    content=file.read()
    print(content)
finally:
    file.close()

#using with
with open(fileName,'r') as file:
    print(file.read())