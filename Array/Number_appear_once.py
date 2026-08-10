def appear_once(arr):
    n = len(arr)
    for i in range(0,n):
        count = 0
        for j in range(0,n):
            if arr[i] == arr[j]:
                count = count + 1
        if count == 1:
            return arr[i]
                    

arr = [1,1,2,3,3,4,4]
print(appear_once(arr))                



