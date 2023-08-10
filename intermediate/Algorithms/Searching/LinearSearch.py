print("Enter the list of Elements:")
data=list(map(int,input().split()))
print("Enter element to be searched:")
searchValue=int(input())

foundAt=-1
for index,value in enumerate(data):
    if value==searchValue:
        foundAt=index
        break
if foundAt>=0:
    print(f"Found at index: {foundAt}")
else:
    print("Not Found!")