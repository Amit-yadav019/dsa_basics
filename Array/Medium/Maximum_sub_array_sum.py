def max_sub_array_sum(arr):
    n = len(arr)
    maximum = float('-inf')
    for i in range(0,n):
                                 # Brute solution
        for j in range(i,n):     # T.C.= O(N^3) near about for wrost case 
                                # S.C. = O(1)
            sum = 0
            for k in range(i,j+1):
                sum = sum + arr[k]
            maximum = max(maximum,sum)  
    return maximum
# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(max_sub_array_sum(arr))        # Brute soln. 



# Better soln.
def max_sub_array_sum(arr):
    n = len(arr)
    maximum = float('-inf')
    for i in range(0,n):
        sum = 0                         # Better solution
        for j in range(i,n):     # T.C.= O(N^2) near about for wrost case 
            sum = sum + arr[j]                    # S.C. = O(1)
            
            
            maximum = max(maximum,sum)  
    return maximum
# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(max_sub_array_sum(arr)) 


# Optimal soultion using Kadane's Algorithm

def max_sub_array_sum_optimal(arr):
    n = len(arr)
    sum = 0
    maximum = float('-inf')
    for i in range(0,n):
        sum = sum+arr[i] # optimal version , T.C. = O(N) and S.C. = O(1)

        if (sum > maximum):
            maximum = sum 
        if (sum< 0):
            sum = 0     
    return maximum
# arr = [-2,-3,4,-1,-2,1,5,-3]
# print(max_sub_array_sum_optimal(arr)) 

# what if the interviewer ask you to print any of those  array of maximum subarray 
# as there can be multiple array having maximum sum 
def max_sub_array_sum_optimal(arr):
    n = len(arr)
    sum = 0
    ans_start = -1
    ans_end = -1 
    maximum = float('-inf')
    for i in range(0,n):
        if sum == 0 :
            start = i 
        sum = sum+arr[i] # optimal version , T.C. = O(N) and S.C. = O(1)

        if (sum > maximum):
            maximum = sum 
            ans_start = start
            ans_end = i 
        if (sum< 0):
            sum = 0     
    return maximum,arr[ans_start:ans_end+1]
arr = [-2,-3,4,-1,-2,1,5,-3]
print(max_sub_array_sum_optimal(arr)) 
