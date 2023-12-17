import unittest
from Scripts.all_python_labs.lab_python_2.functions2 import Calculator

class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiplication(self):
        self.calc.num1 = 10
        self.calc.num2 = 5
        self.calc.operator = '*'
        self.assertEqual(self.calc.calculate(), 50)

    def test_multiplication_with_zero(self):
        self.calc.num1 = 0
        self.calc.num2 = 5
        self.calc.operator = '*'
        self.assertEqual(self.calc.calculate(), 0)

if __name__ == '__main__':
    unittest.main()
