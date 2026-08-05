# Brute soln.
def max_subarray_sum(arr):
    n = len(arr)
 
    max_sum = float('-inf') # to represent -infinity
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum = sum + arr[j]
            max_sum = max(max_sum,sum)

    return max_sum
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print("The max sum of subarray is : ",max_subarray_sum(arr))        

       # T.C. = O(n^2) and S.C. = O(1)


def max_subarray_sum_optimal(arr):
    n = len(arr)
    max_sum = float("-inf")
    sum = 0 
    for i in range(0,n):
        sum = sum + arr[i]
        max_sum = max(max_sum,sum)
        if sum<0:
            sum = 0 
    return max_sum
arr = [-2,1,-3,4,-1,-2,1,-5,4]
print("The max sum of subarray is : ",max_subarray_sum_optimal(arr)) 
