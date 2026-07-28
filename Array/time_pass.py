def missing_5(arr):
    n = len(arr) 
    total_sum = 0
    for i in range (n):
        total_sum = total_sum + arr[i]
    return n*(n+1)//2 - total_sum
arr = [1,3,4,5,2,9,0]    
print(missing_5(arr))


def linear_seach(arr,nums):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == nums :
            
            return i 
    return -1     
    
arr = [5,3,9,8,1,9,11,16,7,8]
nums = int(input("whats the number that you wanted to find : "))  
print(f" The index of given number {nums} is  ", linear_seach(arr,nums))  

print("Git test")
print("Hello Git")