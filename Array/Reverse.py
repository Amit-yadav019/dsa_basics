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