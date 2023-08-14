class SelectionSort:

    def __init__(self,data):
        self.data=data
    
    def sort(self):
        data=self.data
        for i in range(len(data)):
            min=data[i]
            minIndex=i
            for j in range(i,len(data)):
                if data[j]<min:
                    min=data[j]
                    minIndex=j
            if minIndex!=i:
                swap=data[i]
                data[i]=min
                data[minIndex]=swap
        self.data=data

    def display(self):
        for data in self.data:
            print(data,end=" ")
        print("",end="\n")

testData=[21,4,1,3,9,20,25,6,21,14]
ss=SelectionSort(testData)
ss.sort()
ss.display()