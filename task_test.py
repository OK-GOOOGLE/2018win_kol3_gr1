import unittest

from task import Matrix
import math

class MyTest(unittest.TestCase):
	def setUp(self):
		self.head_text = "Matrix"
		self.data1 = [4, 5, 6, 7]
		self.data2 = [2, 2, 2, 1]
		self.test_instance = Matrix(self.data1)

	def test_init(self):
		self.assertEqual(self.test_instance.matrix_size, self, 4)


	