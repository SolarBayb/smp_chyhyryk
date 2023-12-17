import unittest
from Scripts.all_python_labs.lab_python_7.input_parser7 import validate_number


class TestInputParser7(unittest.TestCase):

    def test_validate_number_valid(self):
        self.assertEqual(validate_number("10"), 10)
        self.assertEqual(validate_number("1"), 1)

    def test_validate_number_invalid(self):
        self.assertIsNone(validate_number("0"))
        self.assertIsNone(validate_number("-5"))
        self.assertIsNone(validate_number("abc"))


if __name__ == '__main__':
    unittest.main()
