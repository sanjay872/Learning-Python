def binary_search(input_array, value):
    start=0
    end=len(input_array)-1
    while(True):
        mid=int((start+end)/2)
        midValue=input_array[mid]
        if midValue<value:
            start=mid+1
        elif midValue>value:
            end=mid-1
        else:
            return mid
        if start==mid or end==mid:
            break
    return -1

test_list = [1,3,9,11,15,19,29]
print (binary_search(test_list, 1)) # 0
print (binary_search(test_list, 11)) # 3
print (binary_search(test_list,19)) # 5
print(binary_search(test_list,29)) # 6
print(binary_search(test_list,23)) # -1