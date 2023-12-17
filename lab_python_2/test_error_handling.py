import unittest
from Scripts.all_python_labs.lab_python_2.functions2 import Calculator

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_division_by_zero_error(self):
        self.calc.num1 = 10
        self.calc.num2 = 0
        self.calc.operator = '/'
        result = self.calc.safe_calculate()
        self.assertEqual(result, "Помилка: ділення на нуль!")

    def test_invalid_operator(self):
        self.calc.num1 = 10
        self.calc.num2 = 5
        self.calc.operator = '@'  # Invalid operator
        result = self.calc.safe_calculate()
        self.assertEqual(result, "Помилка: Недійсний оператор")

    def test_sqrt_of_negative_number(self):
        self.calc.num1 = -4
        self.calc.num2 = 2
        self.calc.operator = '√'
        result = self.calc.safe_calculate()
        self.assertEqual(result, "Помилка: Корінь з від'ємного числа не дозволений")

if __name__ == '__main__':
    unittest.main()
