#	input_output.py
#	
#	Created by Dan Hickey 
#	Copyright (c) 2020 DHicks, Danny, DanTheMan
#
# Printing in Python is one of the most fundamental steps in understanding the language.
# Not only is it important to understand how to output characters in the terminal but also utilize it for debugging.


# OUTPUT
# ------

    # Definition: Print Statement
        # An instruction that causes the Python interpreter to display a value on the screen.

# The line below outputs "Python is easy!"
print "Python is easy!"

# The syntax for python 3 is slightly different
#print ("Python is easy!")


# Printing on same line by adding a comma at the end of the print statement
print 'I like',
print 'Python!'

print 'I also enjoy','C++!'

# The syntax for python 3.X is different
# print('I like', end=" ")
# print('Python!')

# Escape Characters
# -----------------

# When displaying text to the terminal you will discover that some characters are not able to be printed.
# Some of these characters include '' or "" and \
# Additionally, you can use a backslash \ in order to access special commands in displaying output.

# \t 	Tab Character - Displays a tab in output
# \n    NewLine Character - Displays a new line in output

# \\	Displays a backslash
# \"	Displays a double quote
# \'	Displays a single quote

print '\'I found a crazy quote!\' exclaimed Dan.\nDan was always a fan of \tP\tU\tN\tS!'

# Output formatting
print '\n'

# You can always use the opposite of double quotes or single quotes to include the other!
print "'I found a crazy quote!' exclaimed Dan.\nDan was always a fan of \tP\tU\tN\tS!"


# INPUT
# -----

    # Definition: prompt 
        # Characters displayed by the interpreter to indicate that it is ready to take input from the user.

# The line below asks the user for input.
raw_input("Enter your favorite number: ")
	
# The syntax for python 3 is slightly different
#input("What is your favorite number: ")


# WRITING / RUNNING SCRIPTS
# -------------------------
# Utilizing the terminal to run a python script.
# 
# Let's try to compile our current file.
# Open your terminal. 
# Navigate to the directory containing the python file. (cd *nameOfDirectory*) or (dir *nameOfDirectory*)
# Run the script. (python input_output.py)


# Commenting Code
# ---------------
# If you haven't noticed already, you can write notes to yourself that do not alter the program.
# You can create a comment in python by using the pound key otherwise known as the hashtag '#'
# Comments are useful for documenting what specific functions do in a program as well as provide notes to other developers or yourself.

# Additionally, you can add multi-line comments using three apostraphes (''')


'''

This is 
a multi-line
comment

'''



