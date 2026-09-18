def Next_Permutation(arr):
    n = len(arr)
    i = n-2 
    while i>=0 and arr[i]>=arr[i+1]: # T.C. = O(N)

                                     # to tack a beakpoint : a element after that all the elements are in decresing order 
        i = i -1                     # here iin our case breakpoint element is '3'

    if i >= 0 :               # T.C. = O(N)
        j = n-1 
        while arr[i]>=arr[j]: # T.C. = O(N)

                              # To search for element just greater that beakpoint element 
            j -=1             # in our case it is '4'

        arr[i],arr[j] = arr[j],arr[i] # swap breakpoint elements and element just larger than breakpont element 

        # Before swapping : arr = [2,3,5,4,1,0,0]
        # after swapping it becomes :  arr = [2,4,5,3,1,0,0]

        # as all the elements are after the breakpoints are in decreasing order that is highest possible 
        # arr = [2,4,|5,3,1,0,0]
    arr[i+1:] = reversed(arr[i+1:]) # # arr = [2,4,|5,3,1,0,0] - # arr = [2,4,|0,0,1,3,5]
    return arr # arr = [2,4,0,0,1,3,5]

arr = [2,3,5,4,1,0,0]     

print(Next_Permutation(arr))

# T.C. = O(N) + O(N) + O(N) = O(3N) = O(N) and S.C. = O(1)
