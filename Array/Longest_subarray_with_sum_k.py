def longest_subarray(arr,k):
    n = len(arr)
    l = 0 
    for i in range(0,n):
        
        for j in range(i,n):
            sum = 0
            for m in range(i,j+1):
                sum = sum + arr[m]
        if sum == m :
            l = max(l,j-i+1)
    return l 
arr = [1,2,3,1,1,1,1,4,2,3]
k = int(input("Enter the value of k : "))
print("The longest sum of subarray with sum k is : ",longest_subarray(arr,k))                

            
