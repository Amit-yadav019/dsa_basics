# Merginig two sorted array 
# let say they are l = [1,2,3,4] & r = [1,1,3,4,,5,6,7]

# # now '
# def merge_arr(l,r):
#     result = []
#     i,j = 0,0
#     m,n = len(l),len(r)
#     while i<m and j<n:
#         if l[i]<=r[j]:
#             result.append(l[i])
#             i = i+1

#         else :
#             result.append(r[j])
#             j = j+1
#     if i<m:
#         result.append(l[i])
#         i = i+ 1
#     if j<n:
#         result.append(r[j])
#         j = j+1
#     return result 
# l = [1,2,3,4]
# r = [1,1,3,4,5,6,7]
# print("The Merging of two array is ",merge_arr(l,r))                


# now let say we have an array , arr = [3,5,2,1,4,,7,9,8]

def merge_sort(arr):
    if len(arr)<=1:
        return arr 

    mid = len(arr)//2
    left_arr = arr[ :mid]
    right_arr = arr[mid: ]
    l = merge_sort(left_arr)
    r = merge_sort(right_arr)

    def merge_arr(l,r):
        i,j = 0,0
        result = []
        m,n = len(l),len(r)

        while i<m and j<n:
            if l[i]<=r[j]:
                result.append(l[i])
                i = i+1
            else :
                result.append(r[j])
                j = j+1
        while i<m:
            result.append(l[i])
            i = i+1
        while j<n:
            result.append(r[j])
            j = j+1
        return result 
    return merge_arr(l,r)
arr = [7,3,9,11,15,19,2,9,1,7]
print("the Merge sorted array is : ", merge_sort(arr))      


# let try to do it in reverse order :

def merge_sort_rev(arr):
    if len(arr)<=1:
        return arr 

    mid = len(arr)//2
    left_arr = arr[ :mid]
    right_arr = arr[mid: ]
    l = merge_sort_rev(left_arr)
    r = merge_sort_rev(right_arr)

    def merge_arr_rev(l,r):
        i,j = 0,0
        result = []
        m,n = len(l),len(r)

        while i<m and j<n:
            if l[i]<=r[j]:
                result.append(r[j])
                j = j+1
            else :
                result.append(l[i])
                i = i+1 
        while i<m:
            result.append(l[i])
            i = i+1
        while j<n:
            result.append(r[j])
            j = j+1
        return result 
    return merge_arr_rev(l,r)
arr = [7,3,9,11,15,19,2,9,1,7]
print("the Merge sorted array in Decreasing order is  : ", merge_sort_rev(arr))

            

        
