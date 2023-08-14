class MergeSort:

    def sort(self,array):
        if len(array) >1:
            mid=len(array)//2
            L=array[:mid]
            M=array[mid:] 

            self.sort(L)
            self.sort(M)
            self.merge(L,M,array)
    
    def merge(self,L,M,array):
            i=0 # first half
            j=0 # second half
            k=0 # len of merged list

            while i<len(L) and j<len(M):
                if L[i]<M[j]:
                    array[k]=L[i]
                    i+=1
                else:
                    array[k]=M[j]
                    j+=1
                k+=1
            
            while i<len(L):
                array[k]=L[i]
                i+=1
                k+=1

            while j<len(M):
                array[k]=M[j]
                j+=1
                k+=1    
            
    def display(self,array):
        for data in array:
            print(data,end=" ")
        print("",end="\n")

testData=[21,4,1,3,9,20,25,6,21,14]
ms=MergeSort()
ms.sort(testData)
ms.display(testData)