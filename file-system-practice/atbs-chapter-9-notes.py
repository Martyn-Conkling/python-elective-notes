from pathlib import Path
# Note that the convention for importing pathlib is to run from pathlib import Path, since otherwise we’d have to enter pathlib.Path everywhere Path shows up in our code.


# Using the Path() function
# if we simply use the Path() function for handling our paths, 
# it will return an object, either WindowsPath() or a PosixPath(), and this will tell us what type of OS we are on and what the string format of the path will be

# if we want to return a string of the path we can simply call the Path() function inside the str() function like so:
print(str(Path('spam', 'bacon', 'eggs')))

# Note if you are running your python code in a unix based terminal or shell on windows, it will return a unix path format



# the / operator that we normally use for division can also combine Path objects and strings. This is helpful for modifying a Path object after you’ve already created it with the Path() function.
# The pathlib module solves these problems by reusing the / math division operator to join paths correctly, no matter what operating system your code is running on. 

# Review Question: Why would we want to use the '/' operator to join paths, instead of string concatination with the '+' operator?
# Answer: Because windows uses backslash '\' instead of forward slash '/' which is used on unix shells, and unix OSs like mac and linux,
#  if you write a script to concatinate paths, you have to always check to see if you are on a windows or unix file system
# using the '/' operator with pathlib allows us to use pathlib to programatically determine what the correct path format will be




# Practical Tasks I want to acomplish

# 1. I want to be able to get the path of a folder or file


# 2. I want to be able to programatically set paths, to navigate my file system to open or save files
