def Next_Permutation(arr):
    n = len(arr)
    i = n-2 
    while i>=0 and arr[i]>=arr[i+1]:
        i = i -1 

    if i >= 0 :
        j = n-1 
        while arr[i]>=arr[j]:
            j -=1

        arr[i],arr[j] = arr[j],arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr

arr = [2,3,5,4,1,0,0]     

print(Next_Permutation(arr))

