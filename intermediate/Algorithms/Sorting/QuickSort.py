class QuickSort:
    
    def sort(self,array,lb,ub):
        if lb<ub:
            loc=self.partition(lb,ub,array)
            self.sort(array,lb,loc-1)
            self.sort(array,loc+1,ub)

    def partition(self,lb,ub,array):
        pivot=array[lb]
        start=lb
        end=ub
        while start<end:
            while(array[start]<=pivot):
                start+=1
            while(array[end]>pivot):
                end-=1
            if(start<end):
                array[start],array[end]=array[end],array[start] # swap of start and end value
        array[lb],array[end]=array[end],array[lb] # swap of pivot and end value
        return end
    
    def display(self,array):
        for data in array:
            print(data,end=" ")
        print("",end="\n")

testData=[21,4,1,3,9,20,25,6,21,14]
qs=QuickSort()
qs.sort(testData,0,len(testData)-1)
qs.display(testData)