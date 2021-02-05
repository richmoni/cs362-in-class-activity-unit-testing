from calculator import add, subtract, multiply, divide
import unittest


class TestCalculator(unittest.TestCase):

    def test_add_valid_positive_inputs(self):
        '''Test add() with valid positive integers'''
        self.assertEqual(add(2, 4), 6, "Should return 6")

    def test_add_valid_negative_inputs(self):
        '''Test add() with valid negative integers'''
        self.assertEqual(add(-2, -4), -6, "Should return -6")

    def test_add_invalid_type(self):
        '''Test add() with an input of invalid type (str)'''
        self.assertEqual(add("This is a string", 4),
                         "Error: Inputs must be integers!", "Should return error message")

    def test_subtract_valid_positive_inputs(self):
        '''Test subtract() with valid positive integers'''
        self.assertEqual(subtract(6, 4), 2, "Should return 2")

    def test_subtract_valid_negative_inputs(self):
        '''Test subtract() with valid negative integers'''
        self.assertEqual(subtract(-6, -4), -2, "Should return -2")

    def test_subtract_invalid_type(self):
        '''Test subtract() with an input of invalid type (str)'''
        self.assertEqual(subtract("This is a string", 4),
                         "Error: Inputs must be integers!", "Should return error message")

    def test_multiply_valid_positive_inputs(self):
        '''Test multiply() with valid positive integers'''
        self.assertEqual(multiply(2, 4), 8, "Should return 8")

    def test_multiply_valid_negative_input(self):
        '''Test multiply() with a valid negative integer and positive integer'''
        self.assertEqual(multiply(-2, 4), -8, "Should return -8")

    def test_multiply_invalid_type(self):
        '''Test multiply() with an input of invalid type (str)'''
        self.assertEqual(multiply("This is a string", 4),
                         "Error: Inputs must be integers!", "Should return error message")

    def test_divide_valid_positive_inputs(self):
        '''Test divide() with valid positive integers'''
        self.assertEqual(divide(4, 2), 2, "Should return 2")

    def test_divide_by_zero(self):
        '''Test divide() with zero for the second operand'''
        self.assertEqual(
            divide(4, 0), "Error: Cannot divide by zero!", "Should return error message")

    def test_divide_invalid_type(self):
        '''Test divide() with an input of invalid type (str)'''
        self.assertEqual(divide("This is a string", 2),
                         "Error: Inputs must be integers!", "Should return error message")


if __name__ == '__main__':
    unittest.main()
