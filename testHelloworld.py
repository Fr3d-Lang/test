import unittest

######       TEST    HELLO    WORLD        #######

######       IMPORT   MYCODE      ######

import mycode

######       CLASS    UNITTEST    ######

class MyFirstTest(unittest.TestCase):

######       FONCTION TEST        ######

	def test_hello(self):
		self.assertEqual(hello_world(), 'hello world')      ######   la fonction hello_world est égale à hello world

	def test_score_joseph(self):
		
		self.assertEqual(scoreCalculation("Joseph",15), "66%")
		

if __name__ == '__main__':
	unittest.main()
