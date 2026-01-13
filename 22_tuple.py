# Tuple in Python
# Immutable in nature
# we can say that list is more useful then right bcz it's mutable ?
# but sometimes in complex projects there might be certain areas, where we don't want change anyhow!
# Means not by negligency or even by mistake, in that case tuple can be useful!


tup = (1, 9, 5, 7, 2)
print(tup, type(tup))

# what if the tuple has only a single element?
# if we don't add an comma it'll be treated as an 'int'
tup2 = (10)   # need to add a comma after the single element
print(tup2, type(tup2))   # the type is int now

# we've to do like this
tup2 = (10,)
print(tup2, type(tup2))   # now the type is tuple


# we can strore multiple data types simultaneously in tuple
tup3 = (2, "Anindya", True, 45.6)
print(tup3)

# Accessing elements in a tuple
print(tup3[1])    # accessing second element
print(tup3[-1])   # accessing last element -> len(tup3)-1 = 4-1 = 3 (in +ve index)


# checking if an element is present in a tuple or not using 'in'

if "Anindya" in tup3:
    print("Yes")
else:
    print("No")


# Slicing in Tuple
# similar to list slicing

tup4 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(tup4[2:5])    # prints elements from index 2 to index 4
print(tup4[::3])    # prints all elements with a jump of 3 index
print(tup4[1:8:2])   # prints elements from index 1 to 7 with a jump of 2 index