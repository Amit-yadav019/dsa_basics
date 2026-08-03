
  # Brute solution 
# def two_sum(arr):
#     n = len(arr)
#     target = int(input("Enter your target value for two sum : "))
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if arr[i] + arr[j] == target :
#                 return i,j
#     return None
# # arr = [5,7,9,1,2,4,15,7,3]
# # print(two_sum(arr))  

# optimal solution 
def two_sum_optimal(arr):
    n = len(arr)
    target = int(input("Enter the target value for two sum : "))
    hash_map = {}
    for i in range(0,n):
        remaining = target - arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[arr[i]] = i
arr = [5,7,9,1,2,4,15,7,3]
print(two_sum_optimal(arr))         

