# Functions in Python

# 1. Built In Functions
# min(), max(), len(), sum(), tyoe(), range(), dict(), list(), tuple(), set(), print(), input(), etc.

# 2. User Defined Functions

def calcGmean(a, b):
    mean = (a*b)/(a+b)
    return mean

# using the same functionalities by calling the function multiple times
# and without rewriting the same lengthy logic over and over again

def isGreater(a, b):
    if(a>b):
        print(a, "is greater than", b)
    elif(a<b):
        print(b, "is greater than", a)
    else:
        print("both are equal")

isGreater(9, 8)
print(calcGmean(9, 8))
isGreater(3, 7)
print(calcGmean(3, 7))


# trick to avoid indentation error in empty functions

def isLesser(a, b):
    pass  # write this if we plan to plan to complete this function in the future

