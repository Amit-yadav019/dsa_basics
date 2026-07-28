# to find the digit of numbers 



      #  EXTRACTION OF DIGIT 
# n = int(input(" Enter any digit : "))
# while n>0 :
#     lastdigit = n%10
#     print(lastdigit,end='')
#     n = n//10 
    
    # GIVEN A NUMBER 'n' find out and return the no. of digits present in a number.


# def num_sum(n):
#     count = 0
#     while n > 0:
#         lastdigit = n%10
#         print(f"  {lastdigit}   ",end='')
        
#         count = count + 1
#         n = n//10
# # if __name__ == "__main__":
# #     n = int(input("Enter any number :"))
# #     num_sum(n)       


def num_sum(n:int):
    count = 0
    while n>0:
        count += 1
        n = n//10
    return count

# if __name__ == "__main__":
#     n = int(input("Enter any number : "))
#     print("number of digit = ",num_sum(n))  


  # TO find the reverse of a number
def num_rev(n:int):
    rev = 0
    while n>0:
        last_digit = n%10 # to find the last digit number 
        rev = (rev*10)+last_digit
        n = n//10
    return rev

# if __name__ == "__main__" :
#     n = int(input("whats the number n is : "))
#     print("The reverse of this given number is :  ",num_rev(n))   


# To find the number of Digit 

def num_digit(n):
    count = 0 
    while n > 0:
        last_digit = n%10
        count = count + 1
        n = n//10
    return count
# if __name__ =="__main__":
#     n = int(input(" whats the number n is here :"))
#     print(" The count of digits in the given number is =  ",num_digit(n))    

# Alternate way by using a Logarithmic function 
import math
def num_digit_log(n):
    
    return int(math.log10(n)+1)
# if __name__ =="__main__":
#     n = int(input(" whats the number n is here :"))
#     print(" The count of digits in the given number is =  ",num_digit_log(n))

def palindrom(n:int):
    rev = 0
    original = n
    while n >0:
        last_digit = n%10
        rev = (rev*10)+last_digit
        n = n//10
    if original == rev:
        print(f" Yes, the given number {rev} is palindrome number  ")
    else :
        print(" Not a palindrome number ")
    return rev
# if __name__ == "__main__":
#     n = int(input(" Enter any number to check for palindrome number "))
#     palindrom(n)        

import math
def armstrong(n:int):
    cube  = 0 
    original = n 
    while n>0 :
        last_digit = n%10
        cube = cube + (last_digit * last_digit * last_digit)
        n = n//10
        
    if original == cube :
        print(f" Yes the given number {n} is a Armstrong Number ")
    else :
        print(" oh no its not a armstrong number ")
    return cube 
# if __name__ == "__main__":
#     n = int(input(" Enter any number to check for palindrome number "))
#     armstrong(n)



# To print all the divisors of a numbers 

def divisors(n):
    for i in range(1,n+1):
        if n%i == 0 :
            print(f" {i} ",end='')
        
# if __name__ == "__main__":
#     n = int(input(" Enter Any number to see the divisors  "))
#     divisors(n)                    

            
        # Alternate way with better T.C. time complexity 
        # 
import math
def divisors2(n:int):
    sqrt = math.isqrt(n)  
  

    for i in range(1,sqrt+1):
        if n%i == 0 :
            print(f" {i} ",end='')
            if ((n//i)!= i):
                
                print(n//i,end='')
    



# if __name__ == "__main__":
#     n = int(input(" Enter Any number to see the divisors  "))
#     divisors2(n)            


# if we wanted it in a sequence in ascending order then 

import math
def divisors2(n:int):
    sqrt = math.isqrt(n)  
    order = []
  

    for i in range(1,sqrt+1):
        if n%i == 0 :
            print(f" {i} ",end='')
            if ((n//i)!= i):
                order.append(n//i)
    for divisors in reversed(order):
        print(f" {divisors} ",end='')            
                
                
    



# if __name__ == "__main__":
#     n = int(input(" Enter Any number to see the divisors  "))
#     divisors2(n)     


import math
def prime(n:int):
    count = 0 
    for i in range(1,n+1):
        if n%i == 0 :
            count = count + 1
    if count == 2:
        print(f" yes the given number {n} is a prime number  ")
    else:
        print(f" the given number {n} is not a prime number ")    
             
# if __name__ == "__main__":
#     n = int(input(" Enter Any number to  check for prime number  "))
#     prime(n)         


    # now with better time complexity 
import math
def prime2(n:int):
    count = 0 
    sqrt = math.isqrt(n)
    for i in range(1,sqrt+1):
        if n%i == 0 :
            count = count + 1  
            if ((n//i) != i) :
                count = count + 1
    if count ==2 :
        print (f" hurray the given number {n} is a prime number ") 
    else :
        print(" ! not a prime number ")

# if __name__ == "__main__":
#     n = int(input(" Enter Any number to  check for prime number  "))
#     prime2(n)               



# now to calculate for GCD( greatest common divisor )
def gcd(n1:int,n2:int):
    gcd = 1
    for i in range(1,min(n1,n2)+1):
        if n1%i == 0 and n2%i == 0 :
            gcd = i
    return gcd

# if __name__ == "__main__":
#     n1 = int(input(" Enter the value of n1 : "))
#     n2 = int(input(" Enter the value of n2 : "))
#     print(" GCD is : ",gcd(n1,n2))

    # Better Approach by using EUCLIDEAN Algorithm
    # i.e. GCD(a,b) = GCD(a-b,b) where a>b.

    # OR GCD(a,b) = GCD(a%b,b) where a > b.
    

def gcd1(n1:int,n2:int):
    gcd = 1 
    while(n1>0 and n2>0):
        if n1>n2:
            n1 = n1%n2
        else :
            n2 = n2%n1
    if n1 == 0 :
        print(n2)  
    else:
        print(n1)


if __name__ == "__main__":
    n1 = int(input(" Enter the value of n1 : "))
    n2 = int(input(" Enter the value of n2 : "))
    gcd1(n1,n2)




        


                          

            


    








