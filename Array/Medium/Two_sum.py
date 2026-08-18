def two_sum(arr):
    n = len(arr)
    Target = int(input("Whats your target value : "))
    for i in range(0,n):
        sum = 0 
        for j in range(i+1,n):
            if Target == arr[i] + arr[j]:
                return i,j
    return False
arr = [2,6,5,8,11]
print(two_sum(arr))        