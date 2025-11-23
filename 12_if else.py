# if else statement in Python

# Conditional Statements
# >, <, >=, <=, ==, !=

# if-else ladder
# Example 1
# a = int(input("Enter your age: "))
# print("Your age is:", a)

# if(a>=18):
#     print("You can drive!")
# else:
#     print("You cannot drive")


# if-elif-else ladder
# Example 2
# num = int(input("Enter a number: "))

# if(num<0):
#     print("The number is negative")
# elif(num==0):
#     print("The number is zero")
# else:
#     print("The number is positive")



# Nested Loop
# Example 3

# num = int(input("Enter a number: "))
# if(num>0):
#     if(num<=10):
#         print("Number is between 1 and 10")
#     elif(num>10 and num<=20):
#         print("Number is between 11 and 20")
#     else:
#         print("Number is greater than 20")
# elif(num<0):
#     print("Number is negative")
# else:
#     print("Number is zero")



# Example 4

import time

hour = int(time.strftime("%H"))
print(hour)

if(hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<18):
    print("Good Afternoon!")
else:
    print("Good Night!")