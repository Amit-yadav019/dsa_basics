def missing(arr):
    n = len(arr)
    arr1 = list(range(n+1))
    for i in range(0,n+1):
        if arr1[i]  not in arr :
            return arr1[i]

arr = [9,6,4,2,3,5,7,0,1]
# print("The missing values in an array is ",missing(arr))         T.C. = 0(n^2) and S.C. = o(n)

# Better soln.

def missing_1(arr):
    n = len(arr)
    for i in range(0,n+1): 
        if i not in arr : # T.c. = 0(n^2) # S.C. = 0(n)

            return i 

arr = [9,6,4,2,3,5,7,0,1]
# print(missing_1(arr))    



# optimal soln.
def missing_2(arr):
    n = len(arr)
    return n*(n+1)//2 - sum(arr) # T.C. = O(1) + O(n) = O(n) and S.C. = O(1)
arr = [0,2,3,5,1,4,6,8,9] 
# print(missing_2(arr))

        # or 

def missing_4(arr):
    n = len(arr) 
    total_sum = 0
    for i in range (n):
        total_sum = total_sum + arr[i]
    return n*(n+1)//2 - total_sum
arr = [1,3,4,5,2,9,8,6,0]    
# print(missing_4(arr))

# applicable  only if there is one missing values

def missing_4(arr):
    n = len(arr) 
    total_sum = 0
    for i in range (n):
        total_sum = total_sum + arr[i]
    return n*(n+1)//2 - total_sum
arr = [1,3,4,5,2,9,8,0]    
# print(missing_4(arr))


def missing_4(arr):
    n = len(arr) 
    total_sum = 0
    for i in range (n):
        total_sum = total_sum + arr[i]
    return n*(n+1)//2 - total_sum
# arr = [1,3,4,5,2,9,0,]    
# print(missing_4(arr))

def missing_5(arr):
    n = len(arr) 
    total_sum = 0
    for i in range (n):
        total_sum = total_sum + arr[i]
    return n*(n+1)//2 - total_sum
arr = [1,3,4,5,2,9,0]    
print(missing_5(arr))



# 
 
        
        
