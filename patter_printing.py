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
# num = int(input("whats the number n : "))
# print1(num)        

def print2(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end='')
        for j in range(0,2*n-2*i-1):
            print("*",end='')
        for j in range(0,i):
            print(" ",end='')
        print()  
# num = int(input("whats number n : "))
# print2(num)    

# print1(5)
# print2(5)

# if __name__ == "__main__":
#     n = int(input("Enter n: "))
#     print2(n)



## NOW WE HAVE TO PRINT THIS PATTERN  

#   *
#.  * *
#.  * * *
#.  * * * *
#.  * * * * *
#.  * * * * 
#.  * * * 
#.  * * 
#.  * 





def print3(n):
    for i in range(1,2*n):
        stars = i 
        if i>n:
            stars = 2*n - i
        for j in range(0,stars):
            print(" * ",end='')
        print()

# if __name__=="__main__":
#     n = int(input("Enter an odd number "))
#     print3(n)


def print4(n):
    for i in range(0,n):
        if i%2 == 0:
            start = 1
        else :
            start = 0
        for j in range(i + 1) :
            print(f"  {start}  ",end='')
            start = 1 - start
        print()
# if __name__=="__main__":
#     n = int(input("Enter an any  number : "))
#     print4(n)                   


def print4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j ,end='')
        for j in range(2*n-2*i):
            print("_",end='')
        for j in range(i,0,-1):
            print(j,end='')

        print()
# if __name__=="__main__":
#     n = int(input("Enter any number : "))
#     print4(n)                
    
    # Output 
# Enter any number : 5
# 1________1
# 12______21
# 123____321
# 1234__4321
# 1234554321

def print5(n):
    num = 1
    for i in range(1,n+1):
       
        for j in range(1,i):
            print(num,end='')
            num = num + 1
        print()
# if __name__ == "__main__":
#     n = int(input("whats the number n : "))
#     print5(n)            

#. OUTPUT 

# whats the number n : 5

# 1
# 23
# 456
# 78910



def print6(n):
    for i in range(1,n+1):
        for j in range(ord('A'),ord('A')+i):
            print(chr(j),end='')
        print()
# if __name__ == "__main__":
#     n = int(input("Whats the number n is : "))
#     print6(n)           


# OUTPUT 
# Whats the number n is : 5
# A
# AB
# ABC
# ABCD
# ABCDE

def print7(n):
    for i in range(1,n+1):
        for j in range(ord('A'),ord('A')+n+1-i):
            print(chr(j),end='')
        print()
# if __name__ == "__main__":
#     n = int(input(" Enter any number : "))
#     print7(n)            


# OUTPUT
#  Enter any number : 5
# ABCDE
# ABCD
# ABC
# AB
# A

def print8(n):
    for i in range(0,n):
        char = chr(ord('A')+i)
        for j in range(1,i+2):
            print(char,end='')
        print()

# if __name__ == "__main__":
#      n = int(input(" Enter any number : "))
#      print8(n)  

               
# OUTPUT 
#  Enter any number : 7
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# GGGGGGG



def print9(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print("_",end='')
        char = chr(ord('A'))
        rev = (2*i +1)//2   
        for j in range(0,2*i+1):
            print(char,end='')
            if j < rev :
                char = chr(ord(char) + 1)
            else :
                char = chr(ord(char) - 1) 
        for j in range(0,n-i-1):
            print("_",end='')
        print()
# if __name__ == "__main__":
#     n = int(input("whats the number n : "))
#     print9(n)   


  # OUTPUT            

# whats the number n : 6
# _____A_____
# ____ABA____
# ___ABCBA___
# __ABCDCBA__
# _ABCDEDCBA_
# ABCDEFEDCBA



def print10(n):
    for i in range(0,n):
        char = chr(ord('A')+n-i-1)




        for j in range(0,i+1):
            print(char,end='')
            char = chr(ord(char) + 1)
        for j in range(0,n-1-i):
            print("_",end='')
        print()

# if __name__ == "__main__":
#     n = int(input("whats the number n : "))
#     print10(n)   




def print11(n):
    for i in range(0,2*n):
        rev = n
        if i<rev:

            for j in range(0,n-i):
                print("*",end="")
            for j in range(0,2*i):
                print(" ",end='')
            for j in range(0,n-i):
                print("*",end='')
        else:
            for j in range(0,i-n+1):
                print("*",end='')
            for j in range(0,4*n - 2*i - 2):
                print(" ",end='')
            for j in range(0,i-n+1):
                print("*",end='')

            
        print()



# if __name__ == "__main__":
#     n = int(input("whats the number n : "))
#     print11(n)      

# OUTPUT

#     whats the number n : 6
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************



def print12(n):
    for i in range(0,2*n-1):
        if i<n:
            stars = i +1
            space = 2*(n-i-1)
        else :
            stars = 2*n-i-1
            space = 2*(i-n+1)
        for j in range(stars):
            print("*",end='')
        for j in range(space):
            print(" ",end='')
        for j in range(stars):
            print("*",end='')
        print()

# if __name__ == "__main__":
#     n = int(input("whats the number n : "))
#     print12(n)

# OUTPUT


#     whats the number n : 7
# *            *
# **          **
# ***        ***
# ****      ****
# *****    *****
# ******  ******
# **************
# ******  ******
# *****    *****
# ****      ****
# ***        ***
# **          **
# *            *




# for prining a square loop 

def print13(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*",end='')

            else:
                print(" ",end='')
        print()

if __name__ == "__main__":
    n = int(input("whats the number n : "))
    print13(n)
        









   
     

      
