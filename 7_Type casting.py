# Type Casting
# conversion of one data type into another data type is known as type casting or type conversion in Python

a = 1
b = 2
print(a+b) # addition = 3

c = "1"
d = "2"
print(c+d) # string concatenation = 12

# Type casting string to integer
e = int(c)
f = int(d)
print(e+f) # addition = 3


# Different types of type casting functions such as:
# int(), float(), str(), chr(), ord(), hex(), oct(), tuple(), list(), set(), dict()
# string is a set of multiple characters

x = "Anindya"
# print(int(x)) # can't convert a string into an int, the string should be valid for type casting

# Types of type casting
# 1. Explicit Type Casting
# user is doing the type casting on his/her own

m = "10"
n = "2"
print(int(m) + int(n)) # 12 -> user is type casting the necessery data types

# 2. Implicit Type Casting
# Python interpreter is doing the type casting on behalf of the user
# Python converts a lower data type to a higher data type automatically in order to avoid data loss
# bool → int → float → complex

x = 10
print(x, type(x)) # int
y = 9.1
print(y, type(y)) # float
print(x+y, type(x+y)) # 19.1 means the value of x automatically converted to float by Python compiler


# bool → int → float → complex
print(5 + True)        # True → int → 1      → 6
print(5 + 3.2)         # int → float         → 8.2
print(3.2 + 2j)        # float → complex     → (3.2+2j)