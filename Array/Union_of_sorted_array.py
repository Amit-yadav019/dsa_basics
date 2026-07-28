# def union(arr1,arr2):
#     temp = []
#     n1 = len(arr1)
#     n2 = len(arr2)
#     for i in range(0,n1-1):
#         if arr1[i] != arr1[i+1] :
#             temp.append(arr1[i])
#     temp.append(arr1[-1])        
            
#     for i in range(0,n2-1) :   
#         if arr2[i] != arr2[i+1] :
#             temp.append(arr2[i])
#     temp.append(arr2[-1])        
            
#     return temp 
# arr1 = [1,1,2,2,3,4,4,4,5,9]
# arr2 = [1,2,3,4,5,6,6,7,8,10]    
# print(union(arr1,arr2))


# # not applicable as in temp we got unsorted array with duplicates 
# # temp = [1, 2, 3, 4, 5, 9, 1, 2, 3, 4, 5, 6, 7, 8, 10]


def union_array(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    result = []
    i = 0
    j = 0

    while i < n1 and j < n2 :
        if arr1[i]<=arr2[j] :
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i = i + 1
        else :
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j = j+ 1
    while i < n1 :
        if len(result) ==0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i = i+1
    while j < n2 :
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j = j+1            
                
    return result 
arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,5,6,7,9,]
# print(f"The union of two array {arr1} and {arr2} is ",union_array(arr1,arr2))      

# Taking array input from users 
def union_array(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    result = []
    i = 0
    j = 0

    while i < n1 and j < n2 :
        if arr1[i]<=arr2[j] :
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i = i + 1
        else :
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j = j+ 1
    while i < n1 :
        if len(result) ==0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i = i+1
    while j < n2 :
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j = j+1            
                
    return result 
arr1 = list(map(int,input("Enter first array element in assending order : ").split()))
arr2 = list(map(int,input("Enter second array element in descending order : ").split()))
print(f"The union of two array {arr1} and {arr2} is ",union_array(arr1,arr2))      




