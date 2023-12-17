import unittest
from Scripts.all_python_labs.lab_python_2.functions2 import Calculator

class TestDivision(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_division(self):
        self.calc.num1 = 10
        self.calc.num2 = 5
        self.calc.operator = '/'
        self.assertEqual(self.calc.calculate(), 2)

    def test_division_by_zero(self):
        self.calc.num1 = 10
        self.calc.num2 = 0
        self.calc.operator = '/'
        self.assertRaises(ZeroDivisionError, self.calc.calculate)

if __name__ == '__main__':
    unittest.main()
