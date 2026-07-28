def intersection(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0 
    result = []
    while i < n1 and j<n2 :
        if arr1[i] < arr2[j]:
            i = i+1
        elif arr2[j]<arr1[i]:
            j = j+1
        else :
            result.append(arr1[i]) 
            i = i+1
            j = j+1       
    
    return result 
arr1 = list(map(int,input("Enter the element for first array ").split()))
arr2 = list(map(int,input("Enter the array element for second array ").split()))     
print(intersection(arr1,arr2))   