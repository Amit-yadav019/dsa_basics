# now to check the index of pivot element first . 

def  partition(arr,low,high):
    pivot = arr[low]
    i,j = low,high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i = i+1
        while arr[j]>pivot and  j>=low+1:
            j = j-1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        P_index = partition(arr,low,high)
        quick_sort(arr,low,P_index -1)
        quick_sort(arr,P_index+1,high)


    
 
 

arr = [10,22,2,5,6,7,0,8]
quick_sort(arr,0,len(arr)-1)
print("sorted array ",arr)  




# T.C. = 0(NlogN), S.C. = 0(1) #for best and avg. case 
# T.C. = 0(N^2) for wrost case i.e. if arr = [5,5,5,5,5,5,5,5]




               
