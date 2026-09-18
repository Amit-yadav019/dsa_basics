  # Brute Solution 

def rearrange_by_sign(arr):
    n = len(arr)
    positive = [] # S.C. = O(n/2)
    negative = [] # S.C. = O(n/2)
    for num in arr:                   ##
        if num > 0 :
            positive.append(num)           ## T.C. = O(n)
        if num < 0 :
            negative.append(num)      ##
    ans = [] # S.C. = O(n)

    # here we have taken len(positive) not len(arr) becoz we are taking two element at once 
    # one positive element at first followed by one negative element . 

    for i in range(len(positive)):  ## T.C. = O(n/2) = O(n)

        ans.append(positive[i])
        ans.append(negative[i])
    return ans                     ## T.C. = O(n) + O(n) = O(2n) 
                                   ## S.C. = O(n/2) + O(n/2) + O(n) = O(2n)
arr = [3,1,-2,-5,2,-4]              
print(rearrange_by_sign(arr))


# Optimal 
def Rearrange_by_sign_optimal(arr):
    ans = [0] * len(arr)
    positive = 0 
    negative = 1

    for num in arr :
        if num > 0 :
            ans[positive] = num 
            positive +=2
        if num < 0 :
            ans[negative] = num 
            negative +=2

    return ans 
# arr = [3,1,-2,-5,-4,2]        
# print(Rearrange_by_sign_optimal(arr))

# 

            
