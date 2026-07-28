def remove_duplicates(arr):
    n = len(arr)
    freq_map = {}

# Step 1: Collect unique elements as dictionary keys
    for i in range(0,n):
        freq_map[arr[i]] = 0


# Step 2: Overwrite the original array with unique keys
    j = 0
    for k in freq_map:
        arr[j] = k
        j = j+1
    return j # Step 3: Return the count of unique elements

# arr = [1,1,1,2,3,4,4,7,9,9,9,10]
# print(remove_duplicates(arr))     

# T.C. = O(2N) and S.C. = O(N)

# now for optimal solution 

def remove_duplicates_optimal(arr):
    n = len(arr)
    if n == 1 :
        return 1 
    i = 0
    j = i+1
    while j<n:
        if arr[j] != arr[i]:
            
            arr[i],arr[j] = arr[j],arr[i]
            i = i+1
        j = j+1
    return i+1
arr = [1,1,1,2,3,4,4,7,9,9,9,10,22,3,2,2,1,7,23]
print(remove_duplicates_optimal(arr))




def remove_duplicates_optimal(arr):
    n = len(arr)
    if n == 1 :
        return 1 
    i = 0
    j = i+1
    while j<n:
        if arr[j] != arr[i]:
            
            arr[i],arr[j] = arr[j],arr[i]
            i = i+1
        j = j+1
    return i+1
arr = [1,1,1,2,3,4,4,7,9,9,9,10,22,3,2,2,1,7,23,57,77,39,69,92,97]
print(remove_duplicates_optimal(arr))
        