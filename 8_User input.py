# taking user input in Python

a = input("Enter your name: ")
print("Ok, so your name is", a)


# By default whatever you paas in input() function,
# it will be considered as string data type
x = input("Enter first number: ")
y = input("Enter second number: ")
print(x+y) # string concatenation

# so type cast it into int
x1 = int(input("Enter first number: "))
y1 = int(input("Enter second number: "))
print(x1+y1) # addition