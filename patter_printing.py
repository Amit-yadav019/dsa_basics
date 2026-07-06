#          * * * *
#          * * * *
#          * * * *
#          * * * *

# for i in range(0,4,1):
#     for j in range(0,4,1):
#         print(" * ",end=' ' )

#     print()



# for taking printing element from users 

# n = int(input("Enter any integers whose square pattern for n index  "))
# p = input(" Enter that you want to print ")
# for i in range(0,n):
#     for j in range(0,n):
#         print(f" {p} ",end=' ')

#     print()    


#.        *
#.        * *
#.        * * *
#.        * * * *
#.        * * * * *

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(" * ", end='')

#     print()    

#  * 
#  *  * 
#  *  *  * 
#  *  *  *  * 
#  *  *  *  *  * 


#.   1 
#.   1 2
#.   1 2 3
#.   1 2 3 4 
#.   1 2 3 4 5
# n = int(input("enter whats n "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f" {j} ",end='')
#     print()    


# n = int(input("enter whats n "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(f" {i} ",end=' ')
#     print()   


#  1
#  2   2
#  3   3   3
#  4   4   4   4
#  5   5   5   5   5
#  6   6   6   6   6   6
#  7   7   7   7   7   7   7
#  8   8   8   8   8   8   8   8  






# n = int(input("whats the values of n : "))
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" * ", end='')

#     print()    

#  *  *  *  *  * 
#  *  *  *  * 
#  *  *  * 
#  *  * 
#  * 



# n = int(input("Enter n : "))
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(f" {j} ", end='')

#     print()    

# Output 
#  0  1  2  3  4 
#  0  1  2  3 
#  0  1  2 
#  0  1 
#  0 



# n = int(input("Enter n : "))
# for i in range(1,n+2):
#     for j in range(1,n+2-i):
#         print(f" {j} ",end='')


#     print()    

# Enter n : 5
#  1  2  3  4  5
#  1  2  3  4
#  1  2  3
#  1  2
#  1     




# n = int(input(" whats the value of n : "))
# for i in range(0,n):

#     for j in range(0,n-i-1):
#        print(" ",end='')
#     for j in range(0,2*i+1):
#         print("*",end='')
#     for j in range(0,n-i-1):
#         print(" ",end='')       
#     print()

#  whats the value of n : 8
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************    
       
    


# n = int(input(" whats the value of n : "))
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end='')
#     for j in range(0,2*n-2*i-1):
#         print("*",end='')
#     for j in range(0,i):
#         print(" ",end='')
#     print()            

#  whats the value of n : 8
# ***************
#  ************* 
#   ***********  
#    *********   
#     *******    
#      *****     
#       ***      
#        *        



# n = int(input(" enter whats the number n is : "))
# for i in range(0,n//2 + 1):
#     for j in range(0,n//2-i):
#         print(" ",end='')
#     for j in range(0,2*i+1):
#         print("*",end='')
#     for j in range(0,n+1/2-i-1):
#         print(" ",end='')
# for i in range(n/2,n):        
#     for j in range(n+1/2-i-1,i):
#         print(" ",end='')
#     for j in range(2*i+1,2*n-2*i-1):
#         print("*",end='')   
#     for j in range(n+1/2-i-1,i):   
#         print(" ",end='')
#     print()    
            


# n = int(input("Enter number: "))

# for i in range(0, n // 2 + 1):
#     for j in range(0, n // 2 - i):
#         print(" ", end="")
#     for j in range(0, 2 * i + 1):
#         print("*", end="")
#     print()

# for i in range(n // 2 - 1, -1, -1):
#     for j in range(0, n // 2 - i):
#         print(" ", end="")
#     for j in range(0, 2 * i + 1):
#         print("*", end="")
#     print()            


# n = int(input("Enter an odd number: "))

# # Upper half
# for i in range(0, n // 2 + 1):
#     # Spaces
#     for j in range(0, n // 2 - i):
#         print(" ", end="")

#     # Stars
#     for j in range(0, 2 * i + 1):
#         print("*", end="")

#     print()

# # Lower half
# for i in range(n // 2 - 1, -1, -1):
#     # Spaces
#     for j in range(0, n // 2 - i):
#         print(" ", end="")

#     # Stars
#     for j in range(0, 2 * i + 1):
#         print("*", end="")

#     print()

def print1(n):
    for i in range(0,n):
        

        for j in range(0,n-i-1):

            print(" ",end='')
        for j in range(0,2*i+1):
            print("*",end='')
        for j in range(0,n-i-1):
            print(" ",end='')
        print()       
num = int(input("whats the number n : "))
print1(num)        

def print2(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end='')
        for j in range(0,2*n-2*i-1):
            print("*",end='')
        for j in range(0,i):
            print(" ",end='')
        print()  
num = int(input("whats number n : "))
print2(num)    

print1(5)
print2(5)








   
     

      
