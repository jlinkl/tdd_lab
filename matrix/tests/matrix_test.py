import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    # Tests


    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    # Test can extract a given row
    def test_extract_full_row(self):
        matrix = Matrix("1 3 4")
        self.assertEqual(matrix.row(3), [1, 3, 4])
    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20
    # def test_extract_double_digits(self):
    #     matrix = Matrix("10 5 4")
    #     self.assertEqual(matrix.row(3), [10, 5, 4])

    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column

    # Test can extract column from a one number matrix

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800



