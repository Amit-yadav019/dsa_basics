def sort(arr):
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(0,n):
        if arr[i]==0:
            count0 = count0 + 1
        elif arr[i] == 1:
            count1 = count1 + 1
        else :
            count2 = count2 + 1
    for i in range(0,count0):
        arr[i] = 0
    for i in range(count0,count0+count1):      
        arr[i] = 1
    for i in range(count1+count0,count0+count1+count2):
        arr[i] = 2
    return arr
arr = [0,1,2,0,1,2,1,2,0,0,1]
print(sort(arr))