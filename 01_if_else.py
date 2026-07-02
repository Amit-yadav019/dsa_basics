# to check either a person is eligible. for voting or not
# print('Enter your Age : ')
# age = int(input())

# age = int(input("Enter your age : "))


# if age >=18:
#     print(f"your age is {age} and you are eligible for Voating ")

# else:
#     print(f'you age is {age} and you are not eligible for voating  !')
    



# school grading system 

# a. Below  25 = try again
# b. 25-40 = E
# c.  40-50 = D
# d.  50 - 60 = C
# e.  60- 70 = B
# f. 70- 80 = A
# g. 80-90 = O
# h. 90-100 = O+  where higher limit is excluded.

# marks = int(input("Enter your marks : "))

# if marks < 25 :
#     print("Try again")

# elif marks >=25 and marks < 40 :
#     print('Grade = E')

# elif 40 <= marks <50:
#     print(' Grade : D')

# elif 50 <= marks <60:
#     print('Grade : C')

# elif 60 <= marks <70:
#     print('Grade : B')

# elif 70 <= marks <80:
#     print('Grade : A')

# elif 80 <= marks <90:
#     print('Grade : O')
# elif 90 <= marks <=100:
#     print('Grade : O+')

# else :
#     print("Invalid marks entered")



## TAKE DAY NUMBER 1 for monday till 7 for sunday from user then print 

# M-1 : by using if else 

# M - 2 : by by import calender 

# import calendar
# day = int(input("ENTER DAY NUMBER FROM 1 - 7 :   "))
# if 1<= day <=7:
#     print(calendar.day_name[day - 1 ])

# else :
#     print(" invalid input")


# by using thinking approach 

# def day_name(day):
#     days = ['Monday','Tuesday','Wednesday','Thusday','Friday','Satuarday','Sunday']
#     if 1<= day <=7 :
#         return days[day-1]

# day = int(input("Enter Day no. from [1-7] :  "))
# print(day_name(day))


# def get_day_name(day_name):
#     days = ['Monday','Tuesday','Wednesday','Thusday','Friday','Satuarday','Sunday']
#     if 1<= day_name <=7 :
#         return days[day_name-1]

# day_name = int(input("Enter Day no. from [1-7] :  "))
# print(get_day_name(day_name))





# def array_01():
#     arr = []

#     print("Enter 5 elements of an array:")
#     for i in range(5):
#         num = int(input(f"Enter element for index {i}: "))
#         arr.append(num)

#     print("Final Array elements:")
#     for i in range(5):
#         print(f"Index {i}: {arr[i]}")

# array_01()
    

# def analyze_string_dsa(input_string):
#     # Step 1: Find the total length (number of characters)
#     # In C++ this is s.size() or s.length()
#     string_len = len(input_string)
#     print(f"The string length is: {string_len}")
    
#     # Step 2: Access the very last character manually using indices
#     # Since indexing starts at 0, the last character is always at (length - 1)
#     last_idx = string_len - 1
#     last_char = input_string[last_idx]
    
#     print(f"The character at index 0 is: {input_string[0]}")
#     print(f"The character at the last index ({last_idx}) is: {last_char}")
    
#     # Step 3: Loop through the string like an array
#     print("Printing characters one by one:")
#     for i in range(string_len):
#         print(f"Index {i}: {input_string[i]}")

# # Calling the function with Striver's exact string
# analyze_string_dsa("Striver")


# OUTPUT
# The string length is: 7
# The character at index 0 is: S
# The character at the last index (6) is: r
# Printing characters one by one:
# Index 0: S
# Index 1: t
# Index 2: r
# Index 3: i
# Index 4: v
# Index 5: e
# Index 6: r


# def striver_multiple(sum_striver):
#     string_len = len(sum_striver)
#     print(f"the character length is {string_len}")

#     last_index = string_len - 1 
#     character = sum_striver[last_index]

#     print(f'the character at index 0 is : {character[0]}')
#     print(f'the character at index 1 is : {sum_striver[1]}')
#     print(f'the character at index 2 is : {sum_striver[2]}')
#     print(f'the character at index 3 is : {sum_striver[3]}')
#     print(f'the character at index 4 is : {sum_striver[4]}')
#     print(f'the character at index 5 is : {sum_striver[5]}')
#     print(f'the character at index 6 is : {sum_striver[6]}')

#     print(f"the character at last index {last_index} is : {character}")


#     print(" NOW PRINTING EACH INDEX WITH CHARACTER ONE BY ONE ")

#     for i in range(string_len):
#         print(f'index{i} : {sum_striver[i]}')


# striver_multiple("shyamsw")


# IF WANTED TO TAKE INPUT DIRRECTLY FROM USERS 
 
# def striver_multiple(sum_striver):
#     string_len = len(sum_striver)
#     print(f"the character length is {string_len}")

#     last_index = string_len - 1 
#     character = sum_striver[last_index]

#     print(f'the character at index 0 is : {character[0]}')
#     print(f'the character at index 1 is : {sum_striver[1]}')
    

#     print(f"the character at last index {last_index} is : {character}")


#     print(" NOW PRINTING EACH INDEX WITH CHARACTER ONE BY ONE ")

#     for i in range(string_len):
#         print(f'index{i} : {sum_striver[i]}')

# user_input = input("Enter any string  :   ")
# input = user_input.strip()
# striver_multiple(input)

# for priniting the name multuple time 

# for i in range (1,10):
#     print(f"Striver")

# if wanted to take input for the message and no. of times from users 

# message = input("Enter , what you want to print :  ")
# times = int(input("how many times you wanted to print : "))

# for i in range ( 1, times+1):
#     print(message)



# Gretting by using functions 

# def names(name):
#     print(f" hello {name} how are you ?")

# name = input("whats your name : ")
# names(name)


# mathematics using functions 

# def calculation(num1 , num2 , operations):
#     if operations == "+":
#         return num1 + num2 

#     elif operations == "-" :
#         return num1 - num2 
#     elif operations == "/":
#         if num2 != 0:
#             return num1/num2 
#         else:
#             return "Error ! : invalid " 
#     elif operations == "*":
#         return num1 * num2 
#     else :
#         return " Invalid input : please inter correct operations "
    
# num1 = int(input("Enter the 1st number : "))
# operations = input("Enter operations among '+', '-'  '/'  '*' ")
# num2 = int(input("enter the 2nd number : "))   

# result = calculation(num1 , num2 , operations)
# print(result)


# for immutable type function 
def do_something(s):
    # s initially points to "raj"
    s = "taj" + s[1:] # Creates a brand NEW string "taj"
    print("Inside function:", s) # Prints "taj"

def main():
    s = "raj"
    do_something(s)
    print("Inside main:", s) # Prints "raj" (Original is untouched!)





# Mutable type Function 

def do_something_mutable(my_list):
    my_list[0] = 't' # Modifies the original object directly

def main():
    s_list = ['r', 'a', 'j']
    do_something_mutable(s_list)
    print("Inside main:", s_list) # Prints ['t', 'a', 'j'] (Original changed!)
















         
        
