# def largest(arr):
#     largest = arr[0]
#     n = len(arr)
#     for i in range(0,n):
#         largest = max(largest,arr[i])
#     return largest

# arr = [1,3,5,67,8,86,2]
# print(largest(arr))

# def largest(arr):
#     largest = arr[0]
#     n = len(arr)
#     for i in range (0,n):
#         if arr[i]>largest :
#             largest = arr[i]
# #     return largest 

# arr = [1,3,5,67,8,86,2]
# # print(largest(arr))    

# def sec_largest(arr):
#     largest = arr[0]
#     n = len(arr)
# arr = [55,75,57,67,31,71,29,78,78]
# n = len(arr)
# arr.sort()
# second_largest = arr[0]
# for i in range(0,n):
#     if arr[n-2] !=arr[n-1]:
#         second_largest = arr[n-2]
#     elif arr[n-2] != arr[n-1]:
#         second_largest = arr[n-2]
#     elif arr[n-3] != arr[n-2]:
#         second_largest = arr[n-3]


    
        
# print(second_largest)    
# wrong approach !



# now optimal way to print the 2nd largest number 

# def largest(arr):
#     largest = arr[0]
#     n = len(arr)
#     for i in range(n):
#         if arr[i]>largest :
#             largest = arr[i]
#     return largest
# def second_largest(arr):
#     largest_element = largest(arr)
#     second_largest = -1
#     n = len(arr)
#     for i in range(0,n):
#         if arr[i]>second_largest and arr[i] !=largest_element:
#             second_largest = arr[i]
#     return second_largest
# arr = [55,75,57,57,87,87,87,54,3,24,5,6,7,7,7,7,7,5]     
# # print("the largest number in the array is :",largest(arr)) 
# # print(" The 2nd largest number in the array is : ",second_largest(arr))  


# Now doing more optimal way 
def largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    n = len(arr)
    for i in range(0,n):
        if arr[i]>largest:
            second_largest = largest 
            largest = arr[i]
        elif arr[i]>second_largest and arr[i] != largest  :
            second_largest = arr[i]
    return second_largest
# arr = [55,75,57,57,87,87,87,54,3,24,5,6,7,7,7,7,7,5,75,75]  
# print(" The 2nd largest number in the array is : ",largest(arr))


# To check either Array is sorted or not 

def sorted(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i+1]>arr[i]:
            continue
        else :
            print(" bumm !  array is not sorted ") 
            return False
    print("Array is sorted ")    
    return True
# arr = [1,2,3,4,5,6,7,8,23,10]
# sorted(arr)

# OR 

def sorted1(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i+1]<arr[i]:
            print(" bumm ! array is not soreted")
            return False
    print(" hurry ! the array is sorted ")
    return True 
arr = [1,2,3,4,5,6,7,8,10]
sorted1(arr)
    
           


        


   
 






    
