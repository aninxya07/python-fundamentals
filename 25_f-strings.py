# String formatting can be done using the format method

letter = "Hey my name is {} and I am from {}"
name = "Anindya"
country = "India"
print(letter.format(name, country))

# or

letter = "Hey my name is {1} and I am from {0}"
name = "Anindya"
country = "India"
print(letter.format(country, name))



# f-strings provide a way to embed expressions inside string literals, using curly braces {}
# f-string method will see the varibale names in the curly brace and try to find upwards where that variable is defined and try to put that variable in place of the curly brace
name = "Anindya"
country = "India"
print(f"Hey my name is {name} and I am from {country}")

print(f"Hey my name is {{name}} and I am from {{country}}")
# if you want to print the curly braces, then you can use double curly braces

# f-strings can also evaluate expressions inside the curly braces
print(f"2*30 = {2*30}")