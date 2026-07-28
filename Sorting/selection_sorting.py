# def selection_sort1(nums):

#     n = len(nums)
#     for i in range(n):
#         mini_index = i
#         for j in range(i+1,n):
#             if nums[j]< nums[mini_index]:
#                 mini_index = j
#         nums[i],nums[mini_index] = nums[mini_index],nums[i] 
#     return nums
# nums = [5,7,8,4,1,6,9,2]          
# print(selection_sort1(nums))



# Now doing it descending order 

# def selection_sort_rev(nums):
#     n = len(nums)
#     for i in range(n-1,-1,-1):
#         max_index = n-1
#         for j in range(n-i,0,1):
#             if nums[i]>nums[max_index]:
#                 max_index = j
#         nums[i],nums[max_index] = nums[max_index],nums[i]        
#     return nums
# nums = [5,7,8,4,1,6,9,2]          
# print(selection_sort_rev(nums))

# sorting in ascending order
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini_index = i 
        for j in range(i+1,n):
            if arr[mini_index] > arr[j]:
                mini_index = j
        arr[i],arr[mini_index] = arr[mini_index],arr[i]
    return arr
# arr =[5,7,2,4,3,1,6]
# print(" the sorted array is :",selection_sort(arr))

# sorting in descending order 
def selection_sort_rev(arr):
    n = len(arr)
    for i in range(n):
        max_index = i 
        for j in range(i+1,n):
            if arr[max_index]<arr[j]:
                max_index = j 
        arr[max_index],arr[i] = arr[i],arr[max_index]   
    return arr
arr =[5,7,2,4,3,1,6]
print(" the sorted array is in reverse order is :",selection_sort_rev(arr))
         
            










