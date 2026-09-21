# # Linear search
# def linear_search(arr, target): # T.C. = O(N)

#     # Check every element of the array
#     for num in arr:

#         # If target is found
#         if num == target:
#             return True

#     # Target was not found
#     return False


# # Brute force solution
# def Longest_consecutive_sequence_brute(arr):   # T.C. = O(N)

#     n = len(arr)

#     # Stores the longest sequence found so far
#     longest = 0

#     # Try every element as the starting point
#     for i in range(0, n):

#         # Current element
#         x = arr[i]

#         # At least the current element itself
#         # is part of the sequence
#         count = 1

#         # Look for the next consecutive number
#         # x + 1
#         while linear_search(arr, x + 1) == True: # T.C. = O(n) * o(n) = O(N^2)

#             # Move to the next number
#             x = x + 1

#             # Increase sequence length
#             count = count + 1

#         # Compare current sequence length
#         # with the longest sequence found so far
#         longest = max(longest, count)

#     return longest


# arr = [102, 4, 100, 1, 1, 101, 3, 2, 2, 1]

# print(Longest_consecutive_sequence_brute(arr))

         
def Linear_search(arr,target): # T.c. = O(n)
    for nums in arr :
        if nums == target :
            return True
    return False

def longest_consecutive_sequence_Brute_soln(arr):
    n = len(arr)
    longest = 0
    for i in range(n): # T.C. = O(n)
        x = 1
        count = 1
        while Linear_search(arr,x+1): # i.e. T.C. = O(n)*O(n) = O(n^2)
            x = x+1
            count +=1
        longest = max(longest,count)
    return longest 
# arr = [102,4,5,100,101,3,1,2,103]
# print("The length of longest consecutive sequence is : ",longest_consecutive_sequence_Brute_soln(arr))   
# for the above Brute force soln. the T.C. = O(n^2) and S.C. = O(1) 

    

# Better soln.
def longest_consecutive_sequence_better(arr):
    n = len(arr)
    arr.sort()
    if n == 0 :
        return 0 
    count = 1
    longest = 1
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            continue
        elif arr[i] == arr[i-1] + 1:
            count = count + 1
        else :
            count = 1
        longest = max(longest,count)
    return longest 
arr = [102,4,5,100,101,3,1,2,103]
print(longest_consecutive_sequence_better(arr))       

# Optimal soln . using set data sequare 

def longest_consecutive_sequence_optimal(arr):
    n = len(arr)
    if n == 0 :
        return 0 
    arr_set = set(arr)
    longest = 1
    for num in arr_set:
        if num -1 not in arr_set:
            count = 1
            x = num
            while x+1 in arr_set:
                x = x + 1
                count = count + 1
            longest = max(longest,count)
    return longest
arr = [102,4,5,100,101,3,1,2,103]
print("for optimal soln : ",longest_consecutive_sequence_optimal(arr))
            


