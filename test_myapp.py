import unittest
from unittest.mock import patch
from io import StringIO
import myapp

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '10', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("The result is: 15.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['2', '10', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("The result is: 5.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['3', '10', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("The result is: 50.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['4', '10', '5', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("The result is: 2.0", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['4', '10', '0', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_division_by_zero(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("Error: Division by zero is not allowed.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['5', '50', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_percentage(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("The result is: 0.5", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['7', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("Invalid choice", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['1', 'a', '6'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        myapp.calculator()
        self.assertIn("Invalid input. Please enter numeric values.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()