#	data_types.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Collective Data Types, otherwise known as Data Structures, consist of lists, dict, tuples, sets, strings and frozensets.
# Data Structures allow for data to be organized, processed and for efficient access or modification of values. 

# Definition: element
    # One of the values in a list (or other sequence), also called items.


####################################################################################################################################

# Adds a space to seperate output
def space():
	print('\n')

####################################################################################################################################


# List
# ----

# Lists allow for data to be placed in a sequential data type.
# Lists have access to methods such as (append(), remove(), pop(), etc.)

# Discover more methods here: https://docs.python.org/2.7/tutorial/datastructures.html

# Definition: List
    # A sequence of values.

# Occupied List
cheese_list = ['Brie', 'Cheddar', 'Mozzarella', 'Swiss'] # Contains 4 elements.

# Empty list
empty_list = [] # Contains no elements.

# Output formatting.
print("Cheeses: ")

# Traversing a list
for cheese in cheese_list:
	print(cheese)

# Traverse through a list to check if a value is inside
print('Bleu' in cheese_list)
print('Cheddar' in cheese_list)


# Adding 'Gouda' and 'String' at the end of the list.
cheese_list.append('Gouda')
cheese_list.append('String')
print(cheese_list)

# Removing 'String' from the list.
cheese_list.remove('String')
print(cheese_list)


# Lists use indexing to acess elements in the list. 
# Our list looks like this below.
#
#	 0		   1		   2		   3        4 
# ['Brie', 'Cheddar', 'Mozzarella', 'Swiss', 'Gouda']
#
# As you can see, the numbers above each type of cheese refers to its 'index' or position in the list.
# Therefore, if you wanted to access the value 'Mozzarella' then you would type 'cheese_list[2]'
print(cheese_list[2]) 

# Lists are also mutable, able to be changed, which can be changed when accessing a value.
cheese_list[1] = 'Parmesan'
print(cheese_list)

# A list slice is when you take a section or slice from a list.
# Using the Table above with values indicating the indexes.
# If I wanted to get the cheeses 'Brie' and 'Cheddar' then it would return a sliced list of ['Brie', 'Cheddar']
two_cheesees = cheese_list[0:2] # If you were to think of this as a domain it would be [0,2) meaning the first number is inclusive and the second is exclusive.
two_cheesees = cheese_list[:2] # This can be implied in python as the domain [0,2)
print(two_cheesees)

# If I wanted to access all of the cheeses past Cheddar.
print(cheese_list[2:5]) # The domain would be [2,5) * Notice that the 5 is equivalent to the length of the list.
print(cheese_list[2:]) # This can be implied in python by not listing the second value.

# Printing the entire list
print(cheese_list[:]) # Therefore this would be implied in python as the domain [0,5)
print(cheese_list)


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# Dictionary (dict)
# -----------------

# A dictionary is very similar to a list; however, a dictionary has the ability to map a 'key' to a specific value.
# Dictionaries also use braces { } rather than square brackets [ ]
#
# Fun Fact! Dictionaries do not have a set order for the elements. 


# Discover more methods here: https://docs.python.org/2.7/tutorial/datastructures.html


# Definition: dictionary
	# A mapping from a set of keys to their corresponding values.

# Empty Dictionary
empty_dict = {}	
empty_dict = dict()
print(empty_dict)

# Defintion: key
	# An object that appears in a dictionary as the first part of a key-value pair.

# A 'key' will be used to 'lookup' a specific value in a dictionary.
# For example in terms of states you would use the key 'IL' to retrieve the value 'Illinois'.
# Another example could be using the key 'AMZM' to retrieve the company 'Amazon' associated with the stock ticker.

states = dict()
states['IL'] = "Illinois"
states['WI'] = "Wisconsin"
print(states)

# Definition: key-value pair
	# The representation of the mapping from a key to a value.

# Additionally, if you want to manually declare and intialize a dictionary you would use.
stock_ticker = {'KO': 'Coca-Cola', 'AMZM': 'Amazon', 'BAC': 'Bank of America', 'TSLA': 'Tesla'}
for stock in stock_ticker.values():
	print(stock)


# Now if you want to retrieve a specific stock you would call it by its key.
print('AMZM: ' + stock_ticker['AMZM'])
print('KO: ' + stock_ticker.get('KO'))

# * Note: You cannot have duplicate keys for a dictionary

# This thinks you are trying to use '0' as a key and therefore returns a KeyError message since '0' isn't a key in our dict.
try:
	print(stock_ticker[0])
except KeyError:
	print('stock_ticker[0] = ' + str(KeyError))


# Checking if a key is inside a dictionary
print(stock_ticker.has_key('AAPL'))
print('TSLA' in stock_ticker)


# You can remove values from a dict too!
stock_ticker.pop('BAC') # Removes key-value pair 'BAC': 'Bank of America'
del stock_ticker['KO'] # Removes key-value pair 'KO': 'Coca-Cola'
print(stock_ticker)

# You can remove a random key-value pair too!
stock_ticker.popitem()
print(stock_ticker)

# You can clear a dictionary too!
stock_ticker.clear()
print(stock_ticker)


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# Tuples
# ------

# Tuples are similar to lists in that they are a sequence of elements; however, the biggest difference between the two is that tuples are immutable (not able to be modified)
# Additionally, tuples are created using the syntax of parenthesis ( ) rather than square brackets [ ] or braces { }.

# Discover more methods here: https://docs.python.org/2.7/tutorial/datastructures.html

# Deinition: tuple
    # An immutable sequence of elements.

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

# Favorite Colors
fav_colors = ("Green", "Blue", "Red")
print(fav_colors)


# You can also created a tuple without parenthesis and just commas.
sports = 'Golf', 'Basketball', 'Football'
print(sports)

# Even if you only plan to have one object intialliy, you must use a comma
favorite_foods = ('Pizza', )
print(type(favorite_foods)) # Prints Tuple

fav_foods = ("Chicken")
print(type(fav_foods))  # Prints String


# Tuples also use indexing to access their values!
#				   0	    1	   2
# fav_colors = ("Green", "Blue", "Red")

print(fav_colors[2])


# Since tuples are immutable you cannot reasign values once they have been intialized.
try:
	fav_colors[1] = "Purple"
except TypeError as err:
	print('fav_colors[1] = "Purple" = {}').format(err)

# Tuple packing is organizing values into a tuple.
# If person_info is a tuple holding values (Name, Age, Height(inches))
person_info = ("Dan", 19, 72.00)

# Tuple unpacking is extracting the values from tuple.
name, age, height = person_info
print("Name: {}, Age: {}, Height: {} inches".format(name,age,height))















