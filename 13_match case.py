# Match Cases in Python (Switch cases in C/C++)

# Example 1

date = int(input("Enter a number (1-7): "))

match date:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    # default case (this will execute if none of the condition matches)
    case _:
        print("Please enter a valid no!")



# Example 2 (Simple Calculator)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")




# Example 3

x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is", x)
    case 4:
        print("x is", x)
    # we can add multiple cases under the default case, whichever matches first in the default section, will get executed first and will exit
    case _ if(x != 90):
        print("x is not 90")
    case _ if(x !=80):
        print("x is not 80")
    case _:
        print("x is", x)
