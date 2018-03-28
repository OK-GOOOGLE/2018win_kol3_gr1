from numpy import *
import time
import threading
from math import sqrt

# new class Matrix
class Matrix:
    def __init__(self, *array):
        if not isinstance(array, tuple):
            raise TypeError('Wrong type - has to be a tuple')

        size = len(array)
        # radical - we give whole size
        self.matrix_size = int(size ** (1 / 2))
        x = self.matrix_size

        # check is it integer or not - true or false
        good_size = (size ** (1 / 2)).is_integer()
        if good_size is False:
            raise ValueError('Wrong size! NOT NxN!')

        # create dynamic matrix using for loop
        self.matrix = [array[i:i + x] for i in range(0, x ** 2, x)]

    # sum two matrix
    @staticmethod
    def add(my_matrix2, my_matrix):
        x = my_matrix2.matrix_size
        y = my_matrix.matrix_size
        if x != y:
            raise ValueError('Wrong size! Left matrix: ' + x + ' Right matrix: ' + y)
        new_matrix = []
        for i in range(y):
            for j in range(y):
                new_matrix.append(my_matrix2.matrix[i][j] + my_matrix.matrix[i][j])
        return Matrix(*new_matrix)

    # sum matrix with one
    @staticmethod
    def add_one(my_matrix2):
        x = my_matrix2.matrix_size
        new_matrix = []
        for i in range(x):
            for j in range(x):
                new_matrix.append(1 + my_matrix2.matrix[i][j])
        return Matrix(*new_matrix)

    # multiply matrix with the other - static method
    @staticmethod
    def multiply(my_matrix2, my_matrix3):
        tab = []
        x = my_matrix2.matrix_size
        y = my_matrix3.matrix_size
        for i in range(x):
            for j in range(y):
                res = sum(my_matrix2.matrix[i][tab] * my_matrix3.matrix[tab][j] for tab in range(x))
                tab.append(res)
        return Matrix(*tab)

    # multiply  matrix with value = 2
    @staticmethod
    def multiply2(my_matrix2):
        return my_matrix2.__mul__(2)

    # create new matrix
    @staticmethod
    def matrix_square(number):
        if not isinstance(number, int):
            raise TypeError("Not a number!")
        closest_square = round(sqrt(number)) ** 2
        a = Matrix._generate_matrix(closest_square)
        return Matrix(*a)

    # generate number from 0 to the max value
    @staticmethod
    def _generate_matrix(number):
        n = 0
        while n < number:
            yield n
            n += 1

    # print
    def __str__(self):
        return str(self.matrix)

    # multiply
    def __mul__(self, argument):
        if isinstance(argument, int):
            return self._multiply_by_number(argument)
        elif isinstance(argument, Matrix):
            return self._multiply_by_matrix(argument)
        else:
            raise TypeError("Unsupported multiple operation")

    def _multiply_by_number(self, argument):
        result = []
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                result.append(self.matrix[i][j] * argument)
        return Matrix(*result)

    def _multiply_by_matrix(self, matrix2):
        x = []
        if self.matrix_size != matrix2.matrix_size:
            raise IndexError("Not equal matrices size")
        for i in range(self.matrix_size):
            for j in range(matrix2.matrix_size):
                x.append(sum(self.matrix[i][x] * matrix2.matrix[x][j] for x in range(self.matrix_size)))
        return Matrix(*x)

    # sum
    def __add__(self, argument):
        if isinstance(argument, int):
            return self._add_number(argument)
        elif isinstance(argument, Matrix):
            return self._add_matrix(argument)
        else:
            raise TypeError("Unsupported add operation")

    def _add_number(self, argument):
        result = []
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                result.append(self.matrix[i][j] + argument)
        return Matrix(*result)

    def _add_matrix(self, matrix2):
        x = []
        if self.matrix_size != matrix2.matrix_size:
            raise IndexError("Not equal matrices size")
        for i in range(self.matrix_size):
            for j in range(matrix2.matrix_size):
                x.append(self.matrix[i][j] + matrix2.matrix[i][j])
        return Matrix(*x)

    def __radd__(self, argument):
        return self.__add__(argument)

    def __rmul__(self, argument):
        return self.__mul__(argument)


matrix_1 = Matrix(4, 5, 6, 7)
matrix_2 = Matrix(2, 2, 2, 1)
#error - matrix is not NxN
#matrix_5 = Matrix(4, 5, 6, 7, 5)
#matrix_6 = Matrix(2, 2, 2, 1, 5)

matrix_3 = Matrix.add(matrix_1, matrix_1)
matrix_4 = Matrix.add(matrix_3, matrix_2)
matrix10 = Matrix.add(matrix_1, matrix_2)
matrix11 = Matrix.add_one(matrix_1)
matrix15 = matrix_1 + matrix_2
matrix18 = matrix_2 * 2
matrix16 = 1 + matrix_2

matrix16 = 1 + matrix_2


print('Matrix')
print(matrix_1)
print(matrix_2)
print('Sum matrix')
print(matrix15)
print(matrix_3)
print(matrix_4)
print(matrix10)
print(matrix11)

print('Multiply matrix - two')
matrix12 = Matrix.multiply(matrix_1, matrix_2)
print(matrix12)
matrix17 = matrix_1 * matrix_2
print(matrix17)
matrix17 = 2 * matrix_2
print(matrix17)
matrix17 = matrix_2 * 2
print(matrix17)


print('Multiply matrix - value = 2')
matrix13 = Matrix.multiply2(matrix_1)
print(matrix13)

print('Create square matrix')
matrix14 = Matrix.matrix_square(18)
print(matrix14)