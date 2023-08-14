class BubbleSort:

    def __init__(self,data):
        self.data=data
    
    def sort(self):
        data=self.data
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j]>data[j+1]:
                    swap=data[j+1]
                    data[j+1]=data[j]
                    data[j]=swap
        self.data=data

    def display(self):
        for data in self.data:
            print(data,end=" ")
        print("",end="\n")

testData=[21,4,1,3,9,20,25,6,21,14]
bs=BubbleSort(testData)
bs.sort()
bs.display()