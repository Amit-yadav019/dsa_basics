# if we wanted to do left rotation of an array '

# def left_rotataion(arr):
#     n = len(arr)
#     arr[:] = arr[1:n] + arr[0:1]
#     return arr
# arr = [ 5,-2,3,9,0,6,10,7]
# print(f"Left Rotate of the array {arr} by one place is ",left_rotataion(arr))

# as of the slicing option is only in python so if we want to do it without using slicing 
# Alternate way '

def left_rotataion02(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr
arr = [5,-2,3,9,0,6,10,7]
print(f"Left Rotate of the array {arr} by one place is ",left_rotataion02(arr))

# T.C. = O(N) and S.C. = O(1)




