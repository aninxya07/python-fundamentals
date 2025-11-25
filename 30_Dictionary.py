# Dictionary in Python
# ordered collection of data items, that are key-value pairs and seperated by commas and enclosed within curly brackets

dic = {
    "Name":"Anindya",
    "Age": 19,
    "Class": "Btech"
}
print(dic)
print(dic["Name"]) # or print(dic.get("Name"))

# in case of accessing a non existing key, it will throw an error in case of first method but will print 'None' in case of .get()


# mapping as emp id and emp name

emp = {
    567: "Anindya",
    361: "Akhil",
    223: "Amit"
}
print(emp[361])
print(emp.keys())    # accessing all the keys
print(emp.values())  # accessing all the values

# printing the dictionary using for loop
for key in emp:
    print(emp[key])

print(emp)   # simplest method of printing dictionary

print(emp.items())   # can use this too for printing the dictionary

# for loop + .items()
for key, value in emp.items():
    print(f"The value corresponding to the {key} is {value}")

