# Recursion = when a function calls itself untill a specific condition is mmet .


# let we have to print hello strivers 10 times using recursion 



def striver10(count):
    
    if count == 10 :
        return 
    print(" Hello , striver ")
    striver10(count+1)

# if __name__ == "__main__":
#     print(striver10(0))



    # recusrsion using parameters 

    # [ print x , n times ]
# def fun(x,n):
#     if n == 0 :
#         return 
#     print(x)
#     fun(x,n-1)
# # fun(7,5)     



# Print 1 to n using recursion 
      # Head recusion 

# def fun2(x,n):
   
    
#     if x>n :
#         return 
#     print(x)
#     fun2(x+1,n)
# fun2(1,10)    

# Now by using tail recursion 
# def fun2(x,n):
#     if x>n:
#         return
#     fun2(x+1,n)
#     print(x)
# fun2(1,3)    
   # OUTPUTS
#    3
#    2
#    1


# now from 1 to n using tail 
# def fun2(x,n):
#     if n > x:
#         return 
#     fun2(x-1,n)
#     print(x)
# fun2(5,1)    

# def fun2(x,n):
#     if x<1:
#         return 
#     fun2(x-1,n)
#     print(x)
# fun2(10,10)    


# for sum of first n natural numbers 
# def num_sum(sum,x,n):
#     if x >n:
#         print("the sum of n natural number from 1 to n is : ",sum)
#         return
#     num_sum(sum + x , x +1,n)
# num_sum(0,1,10)    
    
# def factorial(fact,i,n):
#     if i>n:
#         print(f"The Factorial of given number {n} is ",fact)
#         return
#     factorial(fact*i,i+1,n)
# factorial(1,1,10)        



# Reverse of an array using recursion 
# def rev_array(l,r,arr):
#     if l>=r:
#         return
#     arr[l],arr[r] = arr[r],arr[l]
#     rev_array(l+1,r-1,arr)

# arr = [5,7,3,2,6,1,5,9]
# l = int(input("Enter left position of an array where you wanted to reverese is : "))
# r = int(input("Enter right position of an array where you wanted to reverese is : "))
# # print(" reversing array is ",arr)
# rev_array(l,r,arr)
# print(" reversing array is ",arr)


# def rev_array(l,r,arr):
#     if l>=r:
#         return
#     arr[l],arr[r] = arr[r],arr[l]
#     rev_array(l+1,r-1,arr)

# arr = [5,7,3,2,6,1,5,9]

# # print(" reversing array is ",arr)

# rev_array(2,5,arr)
# print(arr)



# to check for a given string is palindrome or not plindrome 

# def palindome(l,r,arr):
#     if l>=r:
#         return True
#     else:
#         return False
#     arr[l],arr[r] = arr[r],arr[l]
    
#     if arr == rev:
#         print(" the given string is a plaindome",arr)
#     else:
#         print(" no the given string is not a palindome",arr)  
#     palindome(l+)          

# def palindrome(l,r,arr):
#     if l>=r:
#         return True
#     if arr[l] != arr[r] :
#         return False
#     return palindrome(l+1,r-1,arr)

# arr =input("Enter any string ")
# len(arr)

# if palindrome(0,len(arr)-1,arr):
#     print("Palindome ")
# else :
#     print(" not a palindrome")    



# to finding a fabonacci number in a series 
def fabonacci(n):
    if n<=1:
        return n
    return fabonacci(n-1)+fabonacci(n-2)
n = int(input("Enter the index no. to find the fabonacci number :"))
print(fabonacci(n))
        







    



  


