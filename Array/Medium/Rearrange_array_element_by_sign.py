def Rearrange_by_sign(arr):
     
     n = len(arr)
     posIndex = 0 
     negIndex = 1
     ans = [0] *n 
     for i in range(n):
          
          
          if arr[i]<0:
               ans[negIndex] = arr[i]
               negIndex +=2
          else :
               ans[posIndex] = arr[i]
               posIndex +=2
     return ans
arr = [3,1,-2,-5,2,-4]
print(Rearrange_by_sign(arr))

               