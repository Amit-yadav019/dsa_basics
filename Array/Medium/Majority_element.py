def Majority_element(arr):
    n = len(arr)
    for i in range(0,n):
        count = 0 
        for j in range(i,n):
            if arr[i]==arr[j]:
                count = count + 1
        if count>n/2:
            return arr[i]
        
# arr = [2,2,3,3,1,2,2]
# print(Majority_element(arr))    # T.C. = O(n^2) and S.C. = O(1)




# Better solution using Hashmap 

def Majority_element_using_hashmap(arr):
    freq = {}
    n = len(arr)
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num]>n/2:
            return num
    return False

# arr = [2,2,3,3,1,2,2] # T.C. = O(n) and S.C. = O(n)
# print(Majority_element_using_hashmap(arr))




# optimal solution 

def Majority_element_optimal(arr):
    n = len(arr)
    element = None
    count = 0 
    for i in range(n):
        if count == 0 :
            count = 1 
            element = arr[i]
        elif arr[i]==element:
            count +=1
        else:
            count -=1   
    count_1 = 0
    for i in range(n):
        if arr[i]== element:
            count_1 +=1
    if count_1 > n/2:
        return element
    return False
arr = [7,5,5,7,5,7,5,1,5,7,5,7,1,5,1,5,5,5,1]
print(Majority_element_optimal(arr))
                       

        


    
            