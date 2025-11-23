# Different type of List Methods

# 1. Append

marks = [10, 80, 20, 30, 40]
print("Original list:", marks)
marks.append(70)     # appending 70 to the end of the list
print("After append:", marks)


# 2. Sort
marks.sort()
print("After sort:", marks)

marks.sort(reverse=True)
print("After sort in descending order:", marks)


# 3. Reverse
fruits = ["Mango", "Apple", "Banana", "Grapes"]
fruits.reverse()     # reverses the original list (not sorting)
print("After reverse:", fruits)


# 4. Index
print(fruits.index("Mango"))   # returns the index no where "Mango" is present
# print(fruits.index("Blueberry"))  # throws error as "Blueberry" is not present in the list


# 5. Count
numbers = [1, 2, 3, 1, 4, 1, 5, 1]
print("No of times", 1, "is occuring is:", numbers.count(1))


# 6. Copy
new = numbers.copy()
print(new)
new[0] = 70
print(new)


# 7. Insert (for inserting at a particular index not at the end like append)
money = [100, 200, 300, 400, 500]
money.insert(2, 75)   # inserts 75 at index 2
print(money)


# 8. Extend
more_money = [600, 700, 800]
# extends the money list by adding more_money list at the end
money.extend(more_money)
print(money)

# 9. Concatenate
l = [10, 20, 30]
m = [40, 50, 60]

k = l + m  # in extend(), one of the lists were affected, but we want to keep 2 lists as it is, and create a whole new list from this 2
print(k)


# 10. Remove
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.remove("Green")   # removes the first occurance of "Green"
print(colors)

# 11. Pop
removed_item = colors.pop()   # removes the last item and returns it
print("After pop:", colors)
print("Removed item:", removed_item)