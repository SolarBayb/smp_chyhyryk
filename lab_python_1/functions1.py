"""
This module provides a simple calculator application which allows users to perform basic arithmetic operations.
It includes functions for user input, operator validation, and safe calculation, along with a Calculator class for performing calculations.
"""

# Завдання 1: Введення користувача
def get_input():
    """
       Obtain input from the user.

       Asks the user to input two numbers and an operator.

       Returns:
           tuple: A tuple containing two floats (num1, num2) and a string (operator).
    """
    """Отримання введення від користувача."""
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
    return num1, num2, operator

# Завдання 2: Перевірка оператора
def is_valid_operator(operator):
    """
        Check if the given operator is valid.

        Parameters:
            operator (str): The operator to check.

        Returns:
            bool: True if the operator is valid, False otherwise.
    """
    """Перевірка чи оператор є дійсним."""
    valid_operators = ['+', '-', '*', '/', '^', '√', '%']
    return operator in valid_operators

# Завдання 3: Обчислення - включено до класу Калькулятора
class Calculator:
    """
       The Calculator class provides methods to perform basic arithmetic calculations.

       The calculations are performed based on the operator provided by the user. Supported operators include addition (+),
       subtraction (-), multiplication (*), division (/), exponentiation (^), root (√), and modulo (%).
       """

    @staticmethod
    def calculate(num1, num2, operator):
        """
                Perform calculations based on user input.

                Parameters:
                    num1 (float): The first number.
                    num2 (float): The second number.
                    operator (str): The arithmetic operator.

                Returns:
                    float: The result of the arithmetic operation.
        """
        """Виконання обчислень на основі введення користувача."""
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '√':
            return num1 ** (1 / num2)
        elif operator == '%':
            return num1 % num2

# Завдання 5: Обробка помилок
def safe_calculate(num1, num2, operator):
    """
       Safely perform calculations with error handling.

       Parameters:
           num1 (float): The first number.
           num2 (float): The second number.
           operator (str): The arithmetic operator.

       Returns:
           float or str: The result of the arithmetic operation, or an error message if an error occurs.
    """
    """Безпечне виконання обчислень з обробкою помилок."""
    try:
        return Calculator.calculate(num1, num2, operator)
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"
    except Exception as e:
        return f"Помилка: {e}"

# Завдання 10: Налаштування користувача
settings = {
    "decimal_places": 2
}

def update_settings(key, value):
    """
       Update the application settings.

       Parameters:
           key (str): The setting to update.
           value: The new value for the setting.
    """
    """Оновлення налаштувань."""
    settings[key] = value

def get_setting(key):
    """
    Get the value of a specific setting.

    Parameters:
        key (str): The setting to retrieve.

    Returns:
        The value of the setting, if it exists.
    """
    """Отримання значення налаштувань."""
    return settings.get(key)
