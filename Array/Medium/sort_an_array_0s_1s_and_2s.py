def sort(arr): # This is the better solution .
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(0,n):
        if arr[i]==0:
            count0 = count0 + 1
        elif arr[i] == 1:
            count1 = count1 + 1
        else :
            count2 = count2 + 1
    for i in range(0,count0):
        arr[i] = 0
    for i in range(count0,count0+count1):      
        arr[i] = 1
    for i in range(count1+count0,count0+count1+count2):
        arr[i] = 2
    return arr
# arr = [0,1,2,0,1,2,1,2,0,0,1,0,0,1,2]
# print(sort(arr)) 
# Brute solution will be by using merge sort and it will take a T.C. = O(NlogN) and S.C. = O(N)


# Now solving Optimal solution by using 
# # Dutch National Flag Algorithm 
def Sort_optimal(arr):
    n = len(arr)
    low = 0 
    mid = 0 
    high = n - 1
    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low = low +1
            mid = mid +1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high -1 
    return arr
arr = [0,1,2,0,1,2,1,2,0,0,1,0,0,1,2]
print(Sort_optimal(arr))
           

         
            
        
