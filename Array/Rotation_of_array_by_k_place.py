# def rotation_by_k_place(arr):
#     n = len(arr)
#     for i in range(0,k):
#         arr[:] = arr[1:n] + arr[0:1]
#     return arr
# k = int(input("enter the values of K for which place you want to Rotates : "))
# arr = [3,9,5,6,7,2,5,8]
# print(f"the left rotataion of an array{arr} by {k} place is ",rotation_by_k_place(arr))    


# now common and alternate approach 

    

# Better soln. 
# def rotation_by_k_place(arr,k):
#     n = len(arr)
#     k = k%n
    
#     arr[:] = arr[k: ] + arr[ :k]
#     return arr
# k = int(input("enter the values of K for which place you want to Rotates : "))

# arr = [3,9,5,6,7,2,5,8]
# print(f"the left rotataion of an array{arr} by {k} place is ",rotation_by_k_place(arr,k))  


def reverese(arr,left,right):
    while left<right :
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1 
        right = right - 1
    return arr 
arr = [3,9,5,6,7,2,10,9]
left = int(input("enter the values of left : "))    
right = int(input("enter the values of right : "))
print(reverese(arr,left,right))    

# Now we want to left rotation an array by 'k' place 

# let if we want left place by k = 4 from left rotation 
# i.e. for input arr = [3,9,5,6,7,2,10,9]
#  output = , arr = [2,10,9,3,9,5,6,7]

def reverese(arr,left,right):
    while left<right :
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1 
        right = right - 1
    return arr 
def rotate_by_k_place
arr = [3,9,5,6,7,2,10,9]
left = int(input("enter the values of left : "))    
right = int(input("enter the values of right : "))
print(reverese(arr,left,right))    
