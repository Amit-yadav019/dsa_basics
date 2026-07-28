# AVG. / Wrost case 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr            
# arr = [13,46,24,52,20,9]
# print(" the sorted array is ",bubble_sort(arr))     
# 
# Time complexity(T.C.) = O(n^2)
                
#  


def bubble_sort_best_case(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swap = True
        if is_swap ==False:
            return arr
    return arr    
arr = [13,46,24,52,20,9]
print(" the sorted array is ",bubble_sort_best_case(arr))                 



# best case 


def bubble_sort_best_case(arr1):
    n = len(arr1)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
                is_swap = True
        if is_swap ==False:
            return arr1
    return arr1    
arr1 = [2,3,5,7,8,9,12,17]
print(" the sorted array is ",bubble_sort_best_case(arr1))      
# Time complexity(T.C.) = O(n)
                

                


