#	mathematics.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Math is used in functions and operators to modify mutable variables.
# To put simply... Math is math.


# Module
import math

# On line 10, the statement creates a module object named math.

# Definition: module
	# A module is a software component or part of a program that contains one or more routines.

# Modules allow for programmers to be able to able to access its functions and variables.
# To access a function from a module you must follow the following syntax:
# nameOfModule.nameOfFunction()      This is known as dot notation

x = 5.0
y = 2.0
numbers = [1,2,3,4,5]

#Addition
summation = x + y
print(summation)
print(sum(numbers))

#Subtraction
difference = x - y
print(difference)

#Multiplication
product = x * y
print(product)

#Division
quotient = x / y
print(quotient)

#Floor Division
floor_quotient = x // y
print(floor_quotient)

#Inequality Operators
greater_than = x > y
less_than = y < x
greater_than_or_equal_to = x >= y
less_than_or_equal_to = y <= x

#Exponential Operator
print(2**3) # 2^3

#Modulo Operator
print(4 % 2) # Returns 0
print(4 % 3) # Returns 1

#Functions
print(math.sqrt(4))
print(abs(-5))
print(pow(2,3)) # 2^3
print(int(5.0)) # Converts Float to Int


# Discover more of what you can do with math module here
# 	Python 2 : https://docs.python.org/2/library/math.html
# 	Python 3 : https://docs.python.org/3/library/math.html



