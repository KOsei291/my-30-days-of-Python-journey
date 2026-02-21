# Day 5 - Lists
''''
There are four collection data types in Python :
List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.
'''

# There are 2 ways to create lists
lst = list()    # Using list() built in function. This is an empty list
lst_2 = []      # Using square brackets

# We can use len() to find the number of inputs in the list
# Lists can items of different data types
lst_3 = ['Kwabena', 36, True, {'country': 'Ghana', 'city': 'Accra'}]
print(len(lst_3))

# We can also access the inputs using positive or negative indexing
print(lst_3[0])
print(lst_3[-1])
print('\n')

# Next concept, Unpacking. You can unpack a list and give each item a variable
# First example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
print(len(fruits))
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)            # ['lemon','lime','apple']

# Slicing.
print(fruits[0:6])  # Prints all items (in this case, fruits)
print(fruits[::-1]) # Prints in reverse
print(fruits[1:3])  # Prints 2nd and 3rd items
print('\n')

# Modifying Lists
fruits[0] = 'clementine'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'pineapple'
print(fruits)

# Checking items in a list. in is to check if an item is in a list or not
does_exist = 'mango' in fruits
print(does_exist)
print('\n')


# Adding, inserting, and removing items
# For adding, use .append(item) which will add a new item
# For inserting, .insert(index, item) will insert 'item' at the 'index' position
# And for removing, .remove(item) will remove the item. You can use .pop() (it will remove the last item if not specified)
# del is also use to remove items (format: del list_name[index]). Typing del list_name deletes the entire list
fruits.append('banana')
print(fruits)
fruits.insert(3, 'apple')
print(fruits)
fruits.remove('mango')
fruits.pop()
print(fruits)
print('\n')


# You can clear a list using .clear(), copy a list by using .copy and join list by concatenating them (i.e. lst1 + lst2)
# .extend() also joins lists. The format is lst1.extend(lst2)
# .count(item) counts the number of times the input 'item' is in the list
# .index(item) gives you the index of the specific item
# .reverse() reverses the order of a list. Now we don't have to use [::-1]

# We can sort a list using .sort
fruits.sort()   # arranges it in ascending order, in this case, in alphabetical order
print(fruits)
fruits.sort(reverse=True)   # this is in descending order
print(fruits)
