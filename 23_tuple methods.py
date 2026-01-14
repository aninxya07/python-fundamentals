# Different types of methods in Tuple
# we can't perform any changes on a tuple
# we need to change it to a list
# perform changes
# then again need to convert it to a tuple


countires = ("Spain", "Italy", "India", "England", "Germany")
print("Original tuple:", countires)
temp = list(countires)   # converting tuple to list

temp.append("Russia")
# "Spain", "Italy", "India", "England", "Germany", "Russia"

temp.pop(3)     # removing element at index 3
# "Spain", "Italy", "India", "Germany", "Russia"

temp[2] = "Finland"    # modifying at index 2
# "Spain", "Italy", "Finland", "Germany", "Russia"

countires = tuple(temp)   # converting list back to tuple
print("Modified tuple:", countires)


# 1. Tuple Concatenation
countires1 = ("India", "Nepal", "Bhutan")   # tuple1
countires2 = ("USA", "Canada", "Mexico")    # tuple2

earth = countires1 + countires2
print("Concatenated tuple:", earth)


# 2. count()
tup5 = (4, 2, 3, 1, 4, 1, 5, 1)
print("No of times", 1, "is occuring is:", tup5.count(1))


# 3. index()

print(tup5.index(1))   # returns the index no where 1 is present

# we can define a range under a tuple and look for the first occurrence of the element
print(tup5.index(1, 3, 6))   # looks for 1 between index 3 to 5 and returns the first occurrence index
# ans is in 3rd index we found the first 1
# (element, starting range, ending range)


# 4. len()
# tup5 = (4, 2, 3, 1, 4, 1, 5, 1)
    
print("Length of tup5 is:", len(tup5))


# 5. Tuple unpacking
a, b, c = (1, 2, 3)
print(b)  # 2

a, b = (1, 2, 3)
# ValueError: too many values to unpack (expected 2)


a, *b = (1, 2, 3, 4)
print(b)
