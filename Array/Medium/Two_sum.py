def two_sum(arr):
    n = len(arr)
    Target = int(input("Whats your target value : "))
    for i in range(0,n):
        
        for j in range(i+1,n):
            if Target == arr[i] + arr[j]:
                return i,j
    return False
arr = [2,6,5,8,11]
# print(two_sum(arr))     # T.C. = O(N^2) and S.C. = O(1)

# Better soln. using Hashmap Dictonary

def two_sum_better(arr):
    n = len(arr)
    hash_map = {}
    
    for i in range(0,n):
        remaining = Target - arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        else:
            hash_map[arr[i]]= i
    return False
arr = [2,6,5,8,11]
Target = int(input("Enter the target value that you wanted : "))
print(two_sum_better(arr))    