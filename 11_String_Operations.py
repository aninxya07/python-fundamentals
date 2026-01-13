# Different types of String Operations in Python

name = "anindya"
# Strings are immuatble in Python
# means you can't change the characters of a string directly
# but while printing we can use diff string functions in order to change the string

# 1. Upper() and Lower()
print(name.upper())
print(name.lower())


# 2. Strip()
str = "   Blue   "
print(str.strip()) # removes the extra spaces from both ends


# 3. rstrip()
str1 = "!!!Ani!!!!!!!"
print(str1.strip("!")) # removes the specified character from both ends


# 4. Replace()
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
# finds all the occurrences of 'Sp' in the entire string and replaces it with 'M'
# means if there're more than 1 'Sp', then all of them will be replaced by 'M'

str3 = "AaAaaaaA"
print(str3.replace("A", "O"))
print(str3.replace("A", "O", 2))  # changes only first 2 occurrences of 'A' to 'O'


# 5. Split()
# splits the string at each space and returns a list of words
str4 = "Silver Spoon"
print(str4.split(" "))
print(str4.split("e"))   # splits at each occurrence of 'e'


# 6. Title() and Capitalize()
str5 = "hey everyone"
print(str5.title()) # capitalizes first letter of each word
print(str5.capitalize()) # capitalizes only the first letter of the entire string
str6 = "hEy EveRyOne"
print(str6.capitalize()) # also fixes any human error keeping only the first letter capital


# 7. Center() -> to add padding
str7 = "Hello"
print(str7.center(20, "-"))
# centers the string in a field of given width (20 here) and fills the extra space with the specified character (- here)


# 8. Count()
str8 = "banana"
print(str8.count("a"))
# counts the number of occurrences of the specified character in the string


# 9. endswith()
str9 = "Potato"
print(str9.endswith("to")) # True
print(str9.endswith("tu")) # False
print(str9.endswith("to", 2, 10))
# checking if the string "to" exists between the 2nd and the 9th index


# 10. startswith()
str10 = "Cucumber"
print(str10.startswith("Cu")) # True
print(str10.startswith("co")) # False
print(str9.endswith("to", 0, 5))


# 11. find()
str11 = "Watermelon"
print(str11.find("me"))   
# 5 -> first occurrence of "me" otherwise -1 if not found



# 12. index()
# if we want to display an error in case of not finding any substring instead of -1
# then we can use index() in place of find()
# print(str11.index("xy"))  # will display an error


# 13. isalnum()
# checks if all characters in the string are alphanumeric (a-z, A-Z, 0-9) -> return True
# otherwise False -> if there's any special character or space or punctuation

str12 = "Hello123"
print(str12.isalnum()) # True
str13 = "Hello 123!"
print(str13.isalnum()) # False


# 14. isalpha()
# checks if all characters in the string are alphabetic (a-z, A-Z) -> return True
# otherwise False -> if there's any special character or space or punctuation or number

str14 = "Hello"
print(str14.isalpha()) # True
str15 = "Hello123"
print(str15.isalpha()) # False


# 15. islower() and isupper()
str16 = "hello"
print(str16.islower()) # True
str17 = "hEllo"
print(str17.islower()) # False

str18 = "HELLO"
print(str18.isupper()) # True
str19 = "HELLo"
print(str19.isupper()) # False


# 16. isprintable()
str20 = "Hello\nWorld"
print(str20.isprintable()) # False because of \n
str21 = "Hello World"
print(str21.isprintable()) # True


# 17. isspace()
str22 = "   \t\n"
print(str22.isspace()) # True because all are whitespace characters
str23 = "Hello World"
print(str23.isspace()) # False


# 18. swapcase()
str24 = "Hello World"
print(str24.swapcase()) # swaps all the lower cases into upper cases and vice versa


# 19. istitle()
str25 = "Hello World"
print(str25.istitle()) # True
str26 = "Hello world"
print(str26.istitle()) # False as first letter of each word is not capital

