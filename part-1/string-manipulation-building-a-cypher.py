text = "Hello World"
print(text)

# An argument is an object or an expression passed to a function — added between the opening and closing parentheses — when it is called:

# Each string character can be referenced by a numerical index. The index count starts at zero. So the first character of a string has an index of 0. For example, in the string 'Hello World', 'H' is at index 0, 'e' is at index 1, and so on.

# Print the H in "Hello World"
print(text[0])
# Print the W in "Hello World"
print(text[6])


# Python has syntax for referencing characters in strings using negative indexes
# This will print the character 'd'

print(text[-1])

#You can access the number of characters in a string with the built-in len() function.
print(len(text))


#Another useful built-in function is type(), which returns the data type of a variable. Modify your print() call to print the data type of text.

print(type(text))

shift = 3
print(type(shift))


alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower())


index = alphabet.find(text[0].lower())

shifted = alphabet[index+shift]


# Loops in Python
# A loop allows you to systematically go through a sequence of elements and execute actions on each one.
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift

# in Python you can reassign variables different values
# Strings in Python are immmutable
