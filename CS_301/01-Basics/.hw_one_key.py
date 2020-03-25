from hw_one import HW_One
import unittest

class TestHWOneMethods(unittest.TestCase):

	# File name
	FILE_NAME = '.results.csv'

	# Grade problem one.
	def test_problem_1(self):
		ANSWER_ONE = 'I am learning to code in Python!'
		RESULT = '1';
		try:
			self.assertEqual(HW_One().problem_one(), ANSWER_ONE, msg='You answered {}'.format(HW_One().problem_one()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(HW_One().problem_one()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem two.
	def test_problem_2(self):
		ANSWER_TWO = "raw_input('Type in the desired number: ')"
		RESULT = '1'
		try:
			self.assertEqual(HW_One().problem_two(), ANSWER_TWO, msg='You answered {}'.format(HW_One().problem_two()))
		except AssertionError:
			RESULT = '0'
			raise Exception('Incorrect! You answered {}'.format(HW_One().problem_two()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)

	# Grade problem three.
	def test_problem_3(self):
		ANSWER_THREE = '\\/\\/\\/\\/\\/'
		RESULT = '1'
		try:
			self.assertEqual(HW_One().problem_three(), ANSWER_THREE, msg='You answered {}'.format(HW_One().problem_three()))
		except AssertionError:
			RESULT = '0';
			raise Exception('Incorrect! You answered {}'.format(HW_One().problem_three()))
		finally:
			with open(self.FILE_NAME, mode='a') as file:
				file.write(RESULT)


if __name__ == '__main__':
	unittest.main()