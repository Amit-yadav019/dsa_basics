def seperate_zeros_to_right(arr):
    temp = []
    temp2 = []
    n = len(arr)
    for i in range(0,n):
        if arr[i] == 0:
            temp.append(arr[i])
        else :
            temp2.append(arr[i])
    return temp2 + temp
arr =[1,0,2,3,2,0,0,4,5,1]     
# print(seperate_zeros_to_right(arr))   


# optimal solution 
def seperate_zeros_to_right_optimal(arr):
    j = 0 
    n = len(arr)
    for i in range(0,n):
        if arr[i] != 0 :
            arr[j],arr[i] = arr[i],arr[j]
            j = j+1

    return arr
arr =[1,0,2,3,2,0,0,4,5,1]     
print(seperate_zeros_to_right_optimal(arr))  
        



  
