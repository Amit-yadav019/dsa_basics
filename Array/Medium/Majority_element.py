def Majority_element(arr):
    n = len(arr)
    for i in range(0,n):
        count = 0 
        for j in range(i,n):
            if arr[i]==arr[j]:
                count = count + 1
        if count>n/2:
            return arr[i]
        
arr = [2,2,3,3,1,2,2]
print(Majority_element(arr))    
    
            