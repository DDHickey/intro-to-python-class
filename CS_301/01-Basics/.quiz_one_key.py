from quiz_one import Quiz_One
import unittest

class TestHWOneMethods(unittest.TestCase):

	# File name
	FILE_NAME = '.results.csv'
	# Clear contents
	open(FILE_NAME, mode='w').close()


	# Grade problem one.
	def test_problem_1(self):
		ANSWER_ONE = 'C'
		RESULT = '1';
		try:
			self.assertEqual(Quiz_One().problem_one(), ANSWER_ONE, msg='You answered {}'.format(Quiz_One().problem_one()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(Quiz_One().problem_one()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem two.
	def test_problem_2(self):
		ANSWER_TWO = 'B'
		RESULT = '1'
		try:
			self.assertEqual(Quiz_One().problem_two(), ANSWER_TWO, msg='You answered {}'.format(Quiz_One().problem_two()))
		except AssertionError:
			RESULT = '0'
			raise Exception('Incorrect! You answered {}'.format(Quiz_One().problem_two()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem three.
	def test_problem_3(self):
		ANSWER_THREE = 'C'
		RESULT = '1'
		try:
			self.assertEqual(Quiz_One().problem_three(), ANSWER_THREE, msg='You answered {}'.format(Quiz_One().problem_three()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(Quiz_One().problem_three()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem four.
	def test_problem_4(self):
		ANSWER_FOUR = 'D'
		RESULT = '1'
		try:
			self.assertEqual(Quiz_One().problem_four(), ANSWER_FOUR, msg='You answered {}'.format(Quiz_One().problem_four()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(Quiz_One().problem_four()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem five.
	def test_problem_5(self):
		ANSWER_FIVE = 'A'
		RESULT = '1'
		try:
			self.assertEqual(Quiz_One().problem_five(), ANSWER_FIVE, msg='You answered {}'.format(Quiz_One().problem_five()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(Quiz_One().problem_five()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT+'\n')


if __name__ == '__main__':
	unittest.main()