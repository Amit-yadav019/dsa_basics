# Brute soln .
def leader_in_an_array_brute(arr):
    n = len(arr)
    ans = []
    for i in range(0,n):
        leader = True 
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                leader = False
                break
        if(leader== True):
            ans.append(arr[i])
    return ans
arr = [10,22,12,3,0,6]
print(leader_in_an_array_brute(arr))            















# Optimal soln. 
def Leader_in_an_array(arr):
    n = len(arr)
    ans = []
    max_right = arr[n-1] # as last element will be always a leader no any element right of this .
    ans.append(max_right)

    for i in range(n-2,-1,-1): # extacting loop from right to left 

        if arr[i]> max_right:  #checking if any number is greater then max_right i.e. 6 will be our 2nd Leader element 
            ans.append(arr[i])
            max_right = arr[i] # now update max_right as now our max_depth is 2nd learder 
    return ans
arr = [10,22,12,3,0,6]
print(Leader_in_an_array(arr))         # T.C. = O(n) and S.C. = O(1)