# String in Python (Immutable in nature)
# A string is a sequence of characters enclosed within single quotes(' ') or double quotes(" ")

name = "Anindya"
print(name, type(name))
print("Hello " + name)  # string concatenation (manual spacing required)
print("Hello", name) # automated spacing b/w 2 words

apple = 'He said, "I want to eat apples"'
# if you start with "", python interpreter gets confused with the inner ""
# so start with '' and in the middle use "" or vice versa
print(apple)


# Multi Line String
str1 = """Hi, myself Anindya
I'm 21 years old
I'm a software developer"""
print(str1)


# String Indexing (string is like an array of characters but not exactly an array!)
city = "Kolkata"

# left to right 0, 1, 2, ...
print(city[0])  # K
print(city[2])  # l
# print(city[10])  # index out of bound


# right to left -1, -2, -3, ...
print(city[-1]) # a
print(city[-2]) # t
print("\n")

# Looping through a string (will study about loops later on in depth!)
fruit = "Mango"
for char in fruit:
    print(char)