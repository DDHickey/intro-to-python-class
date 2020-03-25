#	files.py
#
#	Created by Dan Hickey
# 	Copyright (c) DHicks, Danny, DanTheMan
#
# Reading and Writing files are important in programming for saving data.

# Definition: directory
	# A named collection of files, also called a folder.

####################################################################################################################################

# Adds a space to seperate output
def space():
	print('\n')

####################################################################################################################################

# When reading or writing to a file, we need to first open the file.
# In order to open a file we need to learn the syntax.

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# Learning the parameters,
# file 					: path-like object (representing a file system path)
# mode (optional) 		: mode while opening a file
# buffering (optional)	: used for setting buffering policy
# encoding (optional)	: the encoding format
# errors (optional)		: string specifying how to handle encoding/decoding errors
# newline (optional)	: how newlines mode works
# closefd (optional)	: must be True (default) otherwise raises an exception
# opener (optional)		: a customer opener

# Usually the syntax is shortened to take two parameters, file and mode.
# open(file, mode='r')


# System Paths 
# ------------

# When opening a file you need to provide a system path to a file.
# Therefore, we need to learn how system paths work!

# There are two types of system paths, absolute and relative.

# Definition: relative path
	# Refers to a location that is relative to a current directory.

relative_path_reading = 'assets/README.txt'
relative_path_writing = 'assets/OUTPUT.txt'

# Definition: absolute path
	# Refers to the complete details needed to locate a file or folder, starting from the root element and ending with the other subdirectories.

absolute_path_reading = '/Users/dan/Documents/Python/CS_301/08-Files/assets/README.txt'
absolute_path_writing = '/Users/dan/Documents/Python/CS_301/08-Files/assets/OUTPUT.txt'


# Mode (parameter)
# ----------------
# Reading 										: 'r'
# Writing 										: 'w'
# Exclusive Creation							: 'x'
# Appending (writing) at end of file			: 'a'
# Open in text mode (default)					: 't'
# Open in binary mode 							: 'b'
# Open a file for updating (read and write)		: '+'



# Reading from a file
# -------------------

# When reading from a file we need to specify the mode as 'reading' or 'r'

# Printing the contents of the file to the terminal.
with open(relative_path_reading, mode='r') as file:
	for line in file:
		print(line),		

# Output formatting.
space()

# Printing the contents of the file on the same line to the terminal.
with open(relative_path_reading, mode='r') as file:
	for line in file:
		print(line.rstrip('\n')),


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# Writing to a file
# -----------------

# When writing from a file we need to specify the mode as 'writing' or 'w'


# Asks for one line of input from the user.
with open(relative_path_writing, mode='w') as file:
	file.write(raw_input("Enter text: "))


# Asks the user for input until the sentinel value of 'done' is reached.
with open(relative_path_writing, mode='w') as file:
	user_input = raw_input("Enter text (type 'done' to end): ")
	while user_input != 'done':
		file.write(user_input)
		user_input = raw_input("Enter text (type 'done' to end): ")
		if (user_input != 'done'):
			file.write('\n')


####################################################################################################################################

# Output formatting.
space()

####################################################################################################################################


# Error Handling
# --------------

# Definition: Error Handling
	# Refers to the anticipation, detection, and resolution of programming, application, and communications errors.

# When writing a program, we want the program to let the user know of any potential issues rather than crashing with no exception.

# You can handle these errors by using a try-except loop

incorrect_path = 'assets/missing.txt'
success = False

# Shows the error of the incorrect path
try:
	with open(incorrect_path, mode='r') as file:
		for line in file:
			print(line),
except IOError as err:
	print(err)
	

# Output formatting.
space()


# Continue looping until user enters correct path.
while success == False:
	try:
		with open(incorrect_path, mode='r') as file:
			for line in file:
				print(line),
			success = True
	except IOError as err:
		print(err)
		incorrect_path = raw_input("Enter new system path: ")













