#	conditionals.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Conditional Statements determine the flow of code through Logical Operators
# They are the bread and butter of creating sophisticated programs.


# Definition: conditional statement
	# A statement that controls the flow of execution depending on some condition.

has_dog = True
num_of_dogs = 2
puppy_name = "Parker"
dog_name = "Beau"

# Checking Conditions
# -------------------

# This conditional statement checks the condition of (has_dog == True) to see if the person owns a dog.
if (has_dog == True):
	print("You must own a dog!")

	# Fun Tip! When checking a condition inside a conditional statement, it is default checked against True
	if (has_dog):
		print("I still can't believe you own a dog!")


if (has_dog == False):
	print("You do not own a dog!")

	# Fun Tip! You can use an exclamation mark in order to reverse the expression.
	if (has_dog != True):
		print("You still do not own a dog!")


# If - Elif - Else
# ----------------

# This is chaining three different conditions into an If, Else If (Elif), Else block.
if (num_of_dogs == 0):
	print("You dont own any dogs!")
elif (num_of_dogs > 0):
	print("You own more than one dog!")
else:
	print("You can't have negative dogs silly!")


# AND
# ---

# You can check multiple conditions inside one conditional statement
if (has_dog == True and num_of_dogs > 0 and dog_name == "Beau" and puppy_name == "Parker"):
	print("You own more than one dog and their names are %s and %s" % (puppy_name, dog_name))

	# *NOTE: When using the keyword 'and' every condition must be True in order for the entire condition to be met.


# OR
# --

if (puppy_name == "Jack" or dog_name == "Beau"):
	print("You must have a dog named Beau or Jack")

	# *NOTE: When using keyword 'or' only one of the conditions must be True in order for the entire condition to be met.
