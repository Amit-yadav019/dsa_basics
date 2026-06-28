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
    

def analyze_string_dsa(input_string):
    # Step 1: Find the total length (number of characters)
    # In C++ this is s.size() or s.length()
    string_len = len(input_string)
    print(f"The string length is: {string_len}")
    
    # Step 2: Access the very last character manually using indices
    # Since indexing starts at 0, the last character is always at (length - 1)
    last_idx = string_len - 1
    last_char = input_string[last_idx]
    
    print(f"The character at index 0 is: {input_string[0]}")
    print(f"The character at the last index ({last_idx}) is: {last_char}")
    
    # Step 3: Loop through the string like an array
    print("Printing characters one by one:")
    for i in range(string_len):
        print(f"Index {i}: {input_string[i]}")

# Calling the function with Striver's exact string
analyze_string_dsa("Striver")








         
        
