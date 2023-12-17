import unittest
from Scripts.all_python_labs.lab_python_2.functions2 import Calculator

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition_positive(self):
        self.calc.num1 = 10
        self.calc.num2 = 5
        self.calc.operator = '+'
        self.assertEqual(self.calc.calculate(), 15)

    def test_addition_negative(self):
        self.calc.num1 = -10
        self.calc.num2 = -5
        self.calc.operator = '+'
        self.assertEqual(self.calc.calculate(), -15)

if __name__ == '__main__':
    unittest.main()
