#Clean the file
file=open("F:/Learning Python/basics/file.txt","w")
file.truncate()

#Write a file
characters=["Luffy","Zoro","Sanji"]
for c in characters:
    file.write(c+'\n')
file.close()

#Read a file
file=open("F:/Learning Python/basics/file.txt","r")
f=file.readlines()

data=[]
for line in f:
    data.append(line.strip())
print(data)