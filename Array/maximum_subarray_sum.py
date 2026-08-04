def max_subarray_sum(arr):
    n = len(arr)
 
    max_sum = float('-inf') # to represent -infinity
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum = sum + arr[j]
            max_sum = max(max_sum,sum)

    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print("The max sum of subarray is : ",max_subarray_sum(arr))        

