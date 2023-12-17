import unittest
from Scripts.all_python_labs.lab_python_2.functions2 import Calculator

class TestSubtraction(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtraction_positive(self):
        self.calc.num1 = 10
        self.calc.num2 = 5
        self.calc.operator = '-'
        self.assertEqual(self.calc.calculate(), 5)

    def test_subtraction_negative(self):
        self.calc.num1 = -10
        self.calc.num2 = -5
        self.calc.operator = '-'
        self.assertEqual(self.calc.calculate(), -5)

if __name__ == '__main__':
    unittest.main()
