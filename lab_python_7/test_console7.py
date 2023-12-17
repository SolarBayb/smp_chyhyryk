import unittest
from Scripts.all_python_labs.lab_python_7.console7 import get_color_code

class TestConsole7(unittest.TestCase):

    def test_get_color_code_valid(self):
        self.assertEqual(get_color_code("1"), '\033[30m')  # Testing for grey color code
        self.assertEqual(get_color_code("8"), '\033[37m')  # Testing for white color code

    def test_get_color_code_invalid(self):
        self.assertEqual(get_color_code("9"), '\033[0m')  # Testing for default color code
        self.assertEqual(get_color_code("abc"), '\033[0m')  # Testing for non-numeric input


if __name__ == '__main__':
    unittest.main()
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
