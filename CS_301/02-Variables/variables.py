#	variables.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# One of the most powerful and used aspects of the Python programming language are variables.
# Variables are mutable values that represent a myriad of different things.


# Rules: variable names can obtain both letters and numbers but must start with a letter.
#	     variable names can be long but should be represented as something useful to the program.
#	     variable names can have uppercase letters however you should start off with a lowercase letter.
#        variables cannot be named as one of the keywords.
#        variables cannot utilize spcialized keyboard characters (!@#$%^&*(){}[]<>?/\|)
#        variables with multi words are often separated with an underscore.


# Python 2 has 31 keywords:
# -------------------------
# and 			del 		from 		not 		while
# as 			elif 		global 		or 			with
# assert 		else 		if 			pass 		yield
# break 		except 		import 		print
# class 		exec 		in 			raise
# continue 		finally 	is 			return
# def 			for 		lambda 		try


# Definition: Syntax
#    The rules that govern the structure of a program


# VARIABLES
# ---------

# string
sentence = "The cow jumped over the moon"
# int
number = 6
# float
pi = 3.141592653589
# boolean
enrolled_in_school = True


# Fun Tip: You can use the function type(*arg*) in order to figure out what type the argument is.
print(type(3.14159))


# String
adjective = "silly"
color = "red"
noun = "cat"

message = adjective + " " + color + " " + noun
print(message)
print("%s %s %s" % (adjective, color, noun))

# boolean
fact = True
law = True
myth = False

print(fact == law)
print(law == myth)

# int | float
sum = 1 + 1
decimal = 1.0 + 1.0
print(sum, decimal)


