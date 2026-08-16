def longest_subarray_with_sum_k(arr,k):
    n = len(arr)
    length = 0
    for i in range(0,n):
        for j in range(i,n):
            sum = 0
            for m in range(i,j+1):
                sum = sum + arr[m]
            if sum == k:
                length = max(length,j-i+1)
    return length 

arr = [1,2,3,1,1,1,1,4,2,3]
k = int(input("whats the value of k :  "))
print(f"The longest subarray with sum {k} is : ",longest_subarray_with_sum_k(arr,k))                

               

            
