import unittest

from task import Matrix


class MyTest(unittest.TestCase):
    def setUp(self):
        self.matrix_1 = Matrix(4, 5, 6, 7)
        self.matrix_2 = Matrix(2, 2, 2, 1)

    def test_init(self):
        self.assertEqual(Matrix(4, 5, 6, 7).matrix_size, self.matrix_1.matrix_size)
        self.assertEqual(Matrix(4, 5, 6, 7).matrix, self.matrix_1.matrix)

    def test_add(self):
        self.assertEqual(Matrix.add(self.matrix_1, self.matrix_2).matrix, [(6, 7), (8, 8)])

    def test_add_one(self):
        self.assertEqual(Matrix.add_one(self.matrix_1).matrix, [(5, 6), (7, 8)])

    def test_add_operator(self):
        self.assertRaises(TypeError, (2, 2, 2, 2))

    def test_mul_operator(self):
        self.assertEqual((self.matrix_1 * self.matrix_2).matrix, [(18, 13), (26, 19)])

    def test_mul_by_number(self):
        self.assertEqual(self.matrix_2._multiply_by_number(2).matrix, [(4, 4), (4, 2)])

    def test_mul_by_matrix(self):
            self.assertEqual(self.matrix_1._multiply_by_matrix(self.matrix_2).matrix, [(18, 13), (26, 19)])

    def test_str(self):
        self.assertEqual(self.matrix_1.__str__(), "[(4, 5), (6, 7)]")

    def test_square(self):
        self.assertEqual(Matrix.matrix_square(18).matrix,
                         [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)])


if __name__ == "__main__":
    unittest.main()
