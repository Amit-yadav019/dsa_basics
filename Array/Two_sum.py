def two_sum(arr):
    n = len(arr)
    target = int(input("Enter your target value for two sum : "))
    for i in range(0,n):
        for j in range(0,n):
            if arr[i] + arr[j] == target :
                return i,j
    return i,j
arr = [5,7,9,1,2,4,15,7,3]
print(two_sum(arr))        