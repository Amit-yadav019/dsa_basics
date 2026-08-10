# Brute solution 
def appear_once(arr):
    n = len(arr)
    for i in range(0,n):
        count = 0
        for j in range(0,n):
            if arr[i] == arr[j]:
                count = count + 1
        if count == 1:
            return arr[i]
                           # T.C. = 0(N^2), S.C. = 0(1)

arr = [1,1,2,3,3,4,4]
# print(appear_once(arr))    
# 
# 


# Better solution 
def appear_once_freq(arr):
    n = len(arr)
    freq = {}

    #Count frequency of each element
    for num in arr :
        freq[num] = freq.get(num,0) + 1


    # find the element that appear only once 
    for num in arr :
        if freq[num] == 1:
            return num
arr = [1,1,2,3,3,4,4]
print("The element that appear only once is : ",appear_once_freq(arr))                






# optimal  solution 
def appear_once_xor(arr):
    n = len(arr)
    result = 0 
    for i in range(0,n):
        result = result ^ arr[i]
    return result
arr = [1,1,2,3,3,4,4] # T.C. = 0(n), S.C. = 0(1)
print("the element which appear once is ",appear_once_xor(arr))    



