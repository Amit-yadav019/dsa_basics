def max_consecutive(arr):
    n = len(arr)
    count = 0 
    max_count = 0
    for num in arr:
        if num == 1:
            count = count + 1 
        else :
            count = 0 
        max_count = max(max_count,count)    
    return max_count
# arr = [1,1,0,1,1,1,0,1,1]
# print("The maximum consective ones are :" ,max_consecutive(arr))    

def max_consecutive1(arr):
    n = len(arr)
    count = 0 
    max_count = 0
    for num in arr:
        if num == 1:
            count = count + 1 
        else :
            count = 0 
        max_count = max(max_count,count)    
    return max_count
arr = [1,1,0,1,1,1,0,1,1]
print("The maximum consective ones are :" ,max_consecutive1(arr))   


