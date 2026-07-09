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

def rev_num(n:int):
    rev = 0
    while n>0:
        lastdigit = n%10
        rev = (rev * 10 )+ lastdigit
        n = n//10
    return rev

if __name__ == "__main__":
    n = int(input("Enter any number : "))
    print("the reverse number is = ",rev_num(n)) 
    

    
  