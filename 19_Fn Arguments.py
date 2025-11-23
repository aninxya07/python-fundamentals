# Function Arguments and Return Statement
# Four types of arguments that we can provide to a function

# 1. Default Arguments
# 2. Keyword Arguments
# 3. Required Arguments
# 4. Variable Length Arguments



# 1. Default Arguments
# while calling the function by the user, if any type of argument is not passed, then the function is called using the default values
# otherwise, if the user enters any value, the default value gets overwritten

def average(a=3, b=5):
    return (a+b)/2

print(average())        # uses default values of a=3 and b=5 and gives result as 4
print(average(10))      # overwrites default value of a with 10, uses default value of b=5 and gives result as 7.5
print(average(10, 20))  # overwrites default values of a and b with 10 and 20 respectively and gives result as 15



# 2. Keyword Arguments

def name(fname, mname, lname):
    print("Hello", fname, mname, lname)

name(fname="Akhil", mname="Kumar", lname="Dolui") # calling function using keyword arguments in same order
name(lname="Dolui", fname="Akhil", mname="Kumar")  # calling function using keyword arguments in different order
name("Akhil", "Kumar", "Dolui")    # calling function using positional arguments in the same order as defined    



# 3. Required Arguments
# When in function signature there's no default value for a parameter and while calling it, we're also not defining it's value, then it throws an error

def calSum(a, b=10):
    print("sum is :", a+b)

# calSum()      # throws error as required argument 'a' is missing
calSum(5)        # b uses default value of 10, a is passed as 5
calSum(5, 15)    # both a and b are passed as 5 and 15 respectively



# 4. Variable Length Arguments
# takes the variable length input as Tuple using 1 star (*numbers)
# can also take as 'Dictionary' using 2 stars (**)

def calMultiplication(*numbers):
    result = 1
    for i in numbers:
        result *= i
    print("Multiplied value is :", result)

# I can paas n no of parameters to the function
calMultiplication(2, 3)               # passing 2 arguments
calMultiplication(2, 3, 4, 5)         # passing 4 arguments
calMultiplication(1, 2, 3, 4, 5, 6)   # passing 6 arguments



# return statement
# Return statement is usde to return the value of the expression back to the calling function

def calSquare(n):
    return n*n   # for 2 return statements by mistake, first one will be considered

x = calSquare(5)
print("Square is :", x)
