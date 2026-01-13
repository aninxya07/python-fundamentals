# String slicing in Python

# 1. String Slicing
names = "Anindya, John, Alice, Bob"
print(names[0:7])  # Slicing: Anindya (always ends with 1 extra index)
print(names[9:13])  # Slicing: John

# 2. String Length
fruit = "Mango"
print(len(fruit))

# 3. String Indexing with Slicing
#  0  1  2  3  4
#  M  a  n  g  o

# positive slicing (left to right)
print(fruit[0:4])
print(fruit[:4]) # python automatically adds the starting 0

print(fruit[2:5])
print(fruit[2:]) # python automatically adds the ending len(fruit)

print(fruit[:]) # prints the whole string from starting to ending == len(fruit)


# Negative slicing (right to left)
#  0  1  2  3  4
#  M  a  n  g  o
# -5 -4 -3 -2 -1

# negative to positive index conversion
# new pos ind = len - neg ind - 1

# new pos ind for '-3' = 5 - 3 - 1 = 1
# will print from 0 to 1st index (we already reduced -1 so not up to 2nd pos ind)
print(fruit[0:-3]) # M to a (-3 means will print 1 lesser which is -4)


# -3 = 5-3 = 2
# -1 = 5-1-1 = 3  (-1 will be reduced only for the ending ind)
# will print from 1 to 3rd pos ind
print(fruit[-3:-1]) # -3 = len(Mango)-3 = 5-3 = 2 & -1 = 5-1 = 4 so 2 to 3 it prints
