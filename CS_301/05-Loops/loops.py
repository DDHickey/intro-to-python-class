#	loops.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Loops are a sequence of instructions that are meant to be repeated until a condition is met.
# Often they are used to simplify a problem or complete a series of actions in a condensed space.


# Definition : iteration
    # Repeated execution of a set of statements using either a recursive function call or a loop.


# Don't feel intimidated if you cannot read all of the code at this point. This is a quick demonstration of how looping can be used in python.

import time

# Count downward from a starting value, waiting one second in between each iteration.
# @param n Refers to the starting value to countdown from.
def countdown(n):
	while (n > 0):
		print n
		time.sleep(1)
		n = n - 1
	print 'Blast Off!'

#countdown(5)

# Adds a space to seperate output
def space():
	print('\n')


# Multiple Assignment
# -------------------

a = 5
b = a
a = 10

print('a = ' + str(a))
print('b = ' + str(b))

# As you can see, after printing the values a = 10 and b = 5
# This is because we intiallially set a to be equal to 5 with (a = 5) 
# and then we intially set b to equal the value of a (b = a) however we next update the value of a by setting it equal to 10 (a = 10)
# Since we do not further update the value of b, it keeps its value of 5 because at the time of intialization a was equal to 5.

# Formatting output.
space()
print('While Loop: ')

# While Loop
# ----------
name = ""
while (name != 'Dan'):
	name = raw_input("Name: ")

# While loops will run until a specific conidtion is met. This value is known as a sentinel value.

# Definition: sentinel value (also referred to as a: flag value, dummy value, signal value)
    # A special value in the context of an algorithm which uses its presence as a condition of termination.

# Formatting output.
space()
print('For Loop: ')

# For Loop
# --------
for i in range(3):
	print(i)

# For loops will run a specific number of times. For loops tend to use values that increment or decrement until it reaches the number of loops given.

# Definition: increment
    # An update that increases the value of a variable (often by one).

# Definition: decrement
    # An update that decreases the value of a variable.


# When to use a For loop vs While loop
# ------------------------------------

# Often people are tasked with completing repetitive actions while getting consistent results. This is where looping becomes imperative to use.
# Usually programmers will use a For loop when they know how many times they need to run a specific task.
    # For example, Writing a program to message every student in a classroom.
        # Writing a program to parse all of your homework from a myriad of websites each class uses.
        # Writing a program to count the number of calories you consumed in a day based on a list of foods you have eaten.
    # In each of these cases you know how many total items are in each situation, however, doing each of these by hand would be tedious.
# On the contrary, programmers tend to use a While loop when they do not know how many iterations it will take the user to find the sentinel value.
    # For example, Writing a program that makes a user guess a number from 1 to 100.
        # Writing a program that will stop running once you guess the user's name.
        # Writing a program that acts as a passcode.
# It may already appear straight forward when to use For loops vs While loops, however, just about every function coded with a While loop can be done with a For loop with modifications if need be.

# Formatting output.
space()
print('Break: ')

# Break
# -----
for i in range(5):
	print(i)
	if (i == 3):
		print("Breaking!")
		break
# From looking at the start of the loop, you would think the loop would run until it reaches 5, however, you can end a loop early by using the keyword 'break'
# Break exits the program from the loop it is contained inside of.

# Formatting output.
space()
print('Continue: ')

# Continue
# --------
for i in range(5):
	if (i == 3):
		print("Continuing!")
		continue
	print(i)

# Continue statements work similar to a break statement, however, instead of exiting the loop entirely
# the program will skip the rest of the code below the continue statement and carry on the loop by incrementing/decrementing.

# Fun Tip! You might have realized by now that during the print statements, the value of 'i' begins at the value '0'. This is because in python, and other languages, the indexing begins at the value '0'.
# This means that the first item in a list will be represented with a 0 and the second value will be represented with a 1 and so on!


