# Sets are unordered collection of data items
# Immutable in nature
# Sets do not contain duplicate items
# written in curly braces


s = {4, 2, 2, 6, 5} # though there're duplicates
print(s, type(s))   # here the duplicates will be gone
# sets internally use hashing, so order is not preserved, anything can happen


# sets can contain diff types of data types
# if you add 1 and 'True' same time, one them will be discarded as both are 1
s1 = {1, "Anindya", False, 4.5}
print(s1, type(s1))


s2 = {}    # trying to create an empty set
print(type(s2))  # <class 'dict'> bcz dict also starts with {}


s3 = set()   # now it's an empty set
print(type(s3))   # <class 'set'>


# accessing the values of a set
s4 = {2, 1, 4, 5, 9, 2, 4, 7}
for value in s4:
    print(value, end=" ")
