# List in Python
# ordered collection of data items
# most popular feature of list is : Mutablity

marks = [30, 50, 60]
print(marks, type(marks))

# length of the list is 3 but index starts from 0
# length = (max index + 1)

print(marks[0])     # accessing first element
print(marks[1])     # accessing second element
# print(marks[3])     # index out of range


# a single list can hold different type of data types

l1 = [10, "Anindya", True, 34.6]
print(l1, type(l1))

# Negative indexing from right to left

print(l1[-1])    # accessing last element
print(l1[-2])    # accessing second last element
print(l1[-3])    # accessing third last element

print(l1[len(l1)-3]) # accessing the same third last element but using positive index
# len(l1)-3 = 4-3 = 1 means positive index 1 = negative third last element

# Check if an item is present in the list using 'in' keyword

l2 = [2, 8, 5, 1, 4]

if 8 in l2:
    print("Yes")
else:
    print("No")

# same thing applies for String as well

# if "Ani" in "Anindya":
#   print("Yes")
# else:
#   print("No")


# Printing all the elements of a list
print(l2)
print(l2[:])    # l2[0:len(l2)]

# list slicing
l3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(l3[1:])     # prints elements from index 1 to end
print(l3[3:6])    # prints elements from index 3 to index 5
print(l3[1:-1])   # -1 = len(l3)-1 = 9-1 = 8 means it'll print from 1 to 7th pos index

# jump index
print(l3[::2])    # prints all elements with a jump of 2 index
print(l3[1:7:2])   # prints elements from index 1 to 6 with a jump of 2 index

lis8 = [1, 2, 3, 4, 5]
print(lis8[1:4][::-1])
# first [1:4] gives -> [2, 3, 4] and over that apply [::-1]
# [start : end : step] here step = -1 means reverse the list
# final output -> [4, 3, 2]


# List Comprehension
# It is used for creating new lists from existing iterables like list, tuple, set, etc.

l4 = [i for i in range(11)]   # creates a list of numbers from 0 to 10
print(l4)

l5 = [i*i for i in range(11)]   # creates a list of squares of numbers from 0 to 10
print(l5)

l6 = [i for i in range(21) if i%2==0]   # creates a list of even numbers from 0 to 20
print(l6)

l7 = [i*i for i in range(21) if i%2==0]   # creates a list of squares of even numbers from 0 to 20
print(l7)



