# 1. Union
s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

# s1 and s2 will stay as it is, only s3 we will get as the union value
s3 = s1.union(s2)
print(s3)


# 2. Update

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}
# take the values from s2 that are not present in s1 and add to s1
# after this, initial s1 will be modified
s1.update(s2)
print(s1)


# 3. Intersection

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s3 = s1.intersection(s2)
print(s3)


# 4. Intersection Update
# take the values that are common in both s1 and s2 and replace in s1, removing rest of the values

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s1.intersection_update(s2)
print(s1)


# 5. Difference
s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s3 = s1.difference(s2)
print(s3)


# 6. Difference update
# keep the difference result in set s1
s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s1.difference_update(s2)
print(s1)



# 7. Symmetric Difference (A U B) - (A n B)
# remove all the common values and then perform union

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s3 = s1.symmetric_difference(s2)
print(s3)


# 8. Symmetric Difference Update
# Keep the result of symmetric difference in set s1

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

s1.symmetric_difference_update(s2)
print(s1)



# 9. Disjoint
# Returns true if both the sets have no common elements

s1 = {1, 2, 5, 7}
s2 = {2, 4, 6, 8}

print(s1.isdisjoint(s2))


# 10. Superset
# if all values of s2 are present inside s1 means s1 is the superset then return True

s1 = {1, 2, 5, 7}
s2 = {2, 5}

print(s1.issuperset(s2))


# 11. Subset
# here we can see clearly s2 is the subset of s1 then it return True
s1 = {1, 2, 5, 7}
s2 = {2, 5}

print(s2.issubset(s1))


# 12. Add

s1 = {1, 2, 5, 7}
s1.add(9)
print(s1)


# 13. Remove/Discard

s1 = {1, 2, 5, 7}
s1.remove(2)   # paas 3 and it'll generate error
print(s1)

s1 = {1, 2, 5, 7}
s1.discard(3)   # it'll not generate error even if 3 is not there in the set
print(s1)

# main difference between remove and discard is that
# remove will throw error if the value is not present in the set
# while discard will not throw error



# 14. Pop
# removes the first item from the set

s1 = {3, 2, 7, 5}
item = s1.pop()
print(s1)
print(item)


# 15. Delete
# removes the entire set along with it's elements

s1 = {3, 2, 7, 5}
del s1
# print(s1)   # will throw an error as s1 is already deleted



# 16. Clear
# only removes all the elements inside the set but preserves the set as it was
s1 = {3, 2, 7, 5}
s1.clear()
print(s1)



# 17. Item existence check

s1 = {3, 2, 7, 5}
print(3 in s1)

# or using loops

if 3 in s1:
    print(3, "is present")
else:
    print(3, "is not present")

