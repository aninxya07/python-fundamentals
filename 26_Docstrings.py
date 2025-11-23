# Docstrings
# These are the string literals that appear right after the definition of a function, method, class or module


def square(n):
    '''takes a number n, and returns the square of the number'''
    return n**2

print(square(5))

print(square.__doc__)


# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the doc attribute.