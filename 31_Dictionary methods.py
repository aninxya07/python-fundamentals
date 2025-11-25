# Different types of dictionary methods in Python

# 1. Update()
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
print(ep1)


# 2. clear()
ep1.clear()
print(ep1)


# 3. Empty dictionary defining
ep3 = {}
print(ep3)


# 4. Pop
ep4 = {122: 45, 123: 89, 567: 69, 670: 69}
ep4.pop(122)    # removes the key 122 along with it's value
print(ep4)


# 5. popitem()
ep4.popitem()    # removes the last key value pair
print(ep4)


# 6. delete
del ep4 # will delete the dict entirely
# print(ep4)   # will throw an error as already been deleted


# 7. delete a single key
ep5 = {122: 45, 123: 89, 567: 69, 670: 69}
del ep5[122]    # key 122 along with it's value gets deleted 
print(ep5)


