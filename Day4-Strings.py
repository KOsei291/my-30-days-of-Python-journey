# Day 4. Strings
"""
This is one of the data types I was introduced to on Day 1. A string can be a single letter or a bunch of letters and words.
You can also find the length of a string by counting the number of characters in the string.
"""

# You can also create a multiline string. You can use single('') or double quotation marks("").
multi_line_string = '''
Hi, I'm Kwabena. This is my 4th python file showing my journey of learning Python.
And this is quite long, but regardless I'm learning and it's fun so I'm cool with it.
'''
print(multi_line_string)
print(len(multi_line_string))

# Next concept. String concatenation.
first_name = 'Kwabena'
last_name = 'Osei'
full_name = first_name + ' ' + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(full_name))


# Escape sequences
print('I am enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote


# String formatting
# Old Style String Formatting (% Operator)
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.(number of digits)f" - Floating point numbers with fixed precision


# New Style String Formatting (str.format)
# {} takes the place of the old style format, and at the end, bring .format() with the variable
# An example 'I am {} {}.'.format(first_name, last_name)
# P.S. for floating points with fixed precision, use {:.(number of digits)f}
print('I am {} {}.'.format(first_name, last_name))

# Another interpolation is using print(f'') by just putting the variable into {} and place the entire print message into f''
# An example is
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')

# Accessing Characters in Strings by Index. Characters in a string are numbered from 0. You can print each character using variable_name[n]
# where n is the index of the character
# An example is
# language = 'Python'
# first_letter = language[0]
# print(first_letter)

# You can also slice strings when printing by using variable_name[n1:n2]
# Reversing the string is done by [::-1]
# Skipping a character can be done by [n0:nl:n] where n0 the first character, nl is the last character, and n is the number of characters it should skip