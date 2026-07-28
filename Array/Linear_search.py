def linear_seach(arr,nums):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == nums :
            
            return i 
    return -1     
    
arr = [5,3,9,8,1,9,11,16,7,8]
nums = int(input("whats the number that you wanted to find : "))  
print(f" The index of given number {nums} is  ", linear_seach(arr,nums))  
         