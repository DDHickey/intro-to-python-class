#	functions.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Functions are a series of statements that performs a desired computation.
# Functions are commonly used to get rid of repetitive code.


# Definition: Function
	# A named sequence of statements that performs some useful operation. 


####################################################################################################################################

# Adds a space to seperate output
def space():
	print('\n')

####################################################################################################################################


# Why should we care about writing functions?
# -------------------------------------------

#	* Easier to read code and debug
# 	* Creates reuseable code
#	* Makes code concise and testable


# Before, we begin writing our own functions, let's understand the syntax of calling functions.

# Type-Conversion functions
# -------------------------
num = int(2.5)
string = str(46)
f_num = float(4)

print('Num: {} String: {} Float: {}'.format(num, string, f_num))

# You have seen functions already defined from the python language.
# print(), len(), raw_input(), type(), etc.


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# User Defined Functions
# ----------------------

# Definition: function definition
	# A statement that creates a new function, specifying its name, parameters, and the statements it executes.

# The syntax for defining a function
# def name_of_function():

# Prints a greeting to the console.
def greeting():
	print('Hello')

# The function 'greeting()' is a user defined function that when 'called' will print "Hello" to the console.
# It is best practice to write a comment above every user-defined function explaining what the function will do.

# Definition: function call
	# A statement that executes a function. It consists of the function name followed by an argument list.

# You need to 'call' a function in order to execute a function.
# Like above, I showed you other instances in which you have already been calling functions.
# The syntax goes as following:  name_of_function()
greeting()


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################

# Returning Values
# ----------------

# Definition: return value
	# The result of a function. If a function call is used as an expression, the return value is the value of the expression.

# Return values are useful in functions when needing to perform a computation.
# You can store the return statements inside of variables for use later in applications.

# A function f(x) used to denote the function 2x + 5.
def f(x):
	return (2 * x) + 5

# f(x) = 2x + 5
# f(5) = 2(5) + 5 = 15

result = f(5)
print("f(5) = {}".format(result))


# Returning Void ('void functions')
# ---------------------------------
# Whenever you do not have a return statement inside a function it is known as a 'void function'
# This is seen inside the greeting function above!

# Prints the sum of two arguments.
def print_sum(a, b):
	sum_result = a + b
	print(sum_result)

void = print_sum(4,5)
print("void = print_sum(4,5) => {}".format(void))

# Fun Fact!
# You must define functions before you can call one.
try:
	print_favColor()			# Throws NameError exception because print_favColor() isnt defined yet.
except NameError as err:
	print(err)

# Prints my favorite color 'Red'
def print_favColor():
	print("Red")


# Uses for functions!
# Calling a function inside another function

# Prints a lyric of a song.
def lyric():
	print("La Di Da")

# Prints all the lyrics of a song.
def song():
	lyric()
	lyric()

print('\nSong: ')
song()


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# Global vs Local variables
# -------------------------

# Definition: local variable
	# A variable defined inside a function. A local variable can only be used inside its function.

# Definition: global variable
	# A variable defined outside a function.

# Prints a global variable 'value'
def print_val():
	print(value)
	return value

# Global variable
value = 1

print_val()
# Compares the two values
print(value == print_val())


# Output formatting.
space()


# Changing a global variable and then prints it
def change_val():
	global new_val	# You need to add a 'global' keyword in order to allow for modifications of global variables in a function.
	print(new_val)
	new_val = 20
	print(new_val)
	return new_val

# Global variable
new_val = 10

change_val()
# Compares the two values
print(new_val == change_val())


# Output formatting.
space()


# Prints a local variable
def show_local():
	val = 5
	print(val)

show_local()
try:
	print(val == show_local())
except NameError as err:
	print(err)









