import os

RESULT_FILE = '.results.csv'
GRADEBOOK_FILE = 'gradebook.txt'

# Clear the contents
open(GRADEBOOK_FILE, mode='w').close()

# Run the grading system for Quiz One
os.system('python -B .quiz_one_key.py')
#os.system('python -B -m unittest -v quiz_one_key')

print('\n\n\n\nNow printing results from homework...\n\n\n\n')

# Run the grading system for HW One
os.system('python -B .hw_one_key.py')
#os.system('python -B -m unittest -v hw_one_key')

# Determine the percentages for File
def determine_percent(FILE_NAME, FILE_TYPE):
	with open(FILE_NAME, mode='r') as file:
		if (FILE_TYPE == 'QUIZ'):
			results = file.readline().rstrip('\n')
		elif (FILE_TYPE == 'HW'):
			results = str(file.readlines()[1]).rstrip('\n')
		else:
			raise Exception('Error reading file.')
		num_Q = len(results)
		num_Corr = 0
		for response in results:
			if (response == '1'):
				num_Corr += 1;
		return int((float(num_Corr) / num_Q) * 100), results

# Determine grade by percentage
def determine_grade(percent):
	if (percent >= 90):
		return 'A'
	elif (percent in range(80,90)):
		return 'B'
	elif (percent in range(70,80)):
		return 'C'
	elif (percent in range(60,70)):
		return 'D'
	return 'F'

# Displays the quiz grades onto gradebook
def display_grades(PERCENT, RESULTS, FILE_TYPE):
	num_Q = len(RESULTS)
	with open(GRADEBOOK_FILE, mode='a') as file:
		if (FILE_TYPE == 'QUIZ'):
			file.write('{} One\t\t\t\t\t{} - {}%'.format(FILE_TYPE, determine_grade(PERCENT), PERCENT));
		elif (FILE_TYPE == 'HW'):
			file.write('{} One\t\t\t\t\t\t{} - {}%'.format(FILE_TYPE, determine_grade(PERCENT), PERCENT));
		else:
			raise Exception('Error reading file.')
		file.write('\n\n')
		for i in range(num_Q):
			file.write('\tProblem {}\t\t\t\t{} / 1\n'.format(i+1, RESULTS[i]))
		if (FILE_TYPE == 'QUIZ'):
			file.write('\n\n')
		else:
			file.write('\n\n\n')

# Displays total grade
def display_total_grade(PERCENTS):
	average = int(sum(PERCENTS) / len(PERCENTS))
	with open(GRADEBOOK_FILE, mode='a') as file:
		file.write('Final Grade:\t{} - {}%'.format(determine_grade(average), average))

# Prints the quiz results to the gradebook
QUIZ_PERCENT, QUIZ_RESULTS = determine_percent(RESULT_FILE, 'QUIZ')
display_grades(QUIZ_PERCENT, QUIZ_RESULTS, 'QUIZ')

# Prints the homework results to the gradebook
HW_PERCENT, HW_RESULTS = determine_percent(RESULT_FILE, 'HW')
display_grades(HW_PERCENT, HW_RESULTS, 'HW')

# Prints the total Grade
PERCENTS = [QUIZ_PERCENT, HW_PERCENT]
display_total_grade(PERCENTS)

# Finished Grading
print('\nImported new grades into gradebook')
