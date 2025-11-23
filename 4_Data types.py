# variables
a = 9
print(a)

b = "Anindya" # in double quotes bcz to differentiate it's a string, not a varibale named Anindya
print(b)

c = 1 # int
d = True # bool
e = "Ani" # string
f = None # NoneType
g = 8.6 # float
h = complex(8, 2) # 8+2j -> complex no

print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))


# collection of multiple data types
# Mutable in nature
list1 = [1, [-2, 7], "apple", [2.3, 4], "banana"]
print(list1, type(list1))

# tuple - Immutable in nature
tuple1 = (1, 2, 3, ("apple", "banana"), 4.5)
print(tuple1, type(tuple1))

# collection of key value pairs
dict1 = {"name" : "Anindya", "age" : 21, "canVote" : True}
print(dict1, type(dict1))


# everything you make or define in Python is an object,
# it can be an int obj, str obj, dictionary obj etc.
