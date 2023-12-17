from Scripts.all_python_labs.shared_lib.calculation_functions import CalculationFunctions
from Scripts.all_python_labs.shared_lib.memory_manager import MemoryManager
from Scripts.all_python_labs.shared_lib.history_logger import HistoryLogger
from Scripts.all_python_labs.shared_lib.api_client import APIClient
from Scripts.all_python_labs.shared_lib.data_manager import DataManager
from Scripts.all_python_labs.shared_lib.input_validator import InputValidator
from prettytable import PrettyTable
import logging

class ConsoleUI:
    def __init__(self, api_client=None):
        self.api_client = api_client
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Додавання обробника логування
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    #lab1
    def choose_task(self):
        self.logger.info("Запуск вибору завдання користувачем")
        """Дозволяє користувачеві вибрати завдання для виконання."""
        calculation_functions = CalculationFunctions()
        memory_manager = MemoryManager()
        history_logger = HistoryLogger()

        while True:
            print("\nВиберіть завдання для виконання:")
            print("1: Введення користувача і обчислення")
            print("2: Перевірка історії обчислень")
            print("3: Отримання значення з пам'яті")
            print("4: Вихід з програми")

            choice = input("Ваш вибір: ")

            if choice == "1":
                if choice == "1":
                    calculation_functions.get_input()  # Використовуйте метод get_input() екземпляра calculator_functions
                    while not calculation_functions.is_valid_operator():
                        print("Недійсний оператор. Спробуйте ще раз.")
                        calculation_functions.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
                    result = calculation_functions.safe_calculate()
                    print(f"Результат: {result}")

            elif choice == "2":
                history_logger.view()

            elif choice == "3":
                value = memory_manager.retrieve()
                print(f"Значення у пам'яті: {value}")

            elif choice == "4":
                print("Вихід з програми.")
                break

            else:
                print("Невідомий вибір. Спробуйте ще раз.")

#lab2

    def run_calculator(self):
        self.logger.info("Запуск калькулятора")
        calc = CalculationFunctions()
        while True:
            calc.get_input()
            while not calc.is_valid_operator():
                print("Недійсний оператор. Спробуйте ще раз.")
                calc.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            result = calc.safe_calculate()
            print(f"Результат: {result}")
            if not calc.repeat_calculation():
                break

#lab3


    @staticmethod
    def get_input(prompt):
        logging.info(f"Отримання введення: {prompt}")
        return input(prompt)

    def choose_option(self, options, prompt="Виберіть опцію: "):
        while True:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print(f"Будь ласка, виберіть число від 1 до {len(options)}")
            except ValueError:
                print("Введено невірний формат. Будь ласка, введіть номер.")

    def print_colored_text(self, text, color):
        print(text, end="", flush=True)

    def print_message(self, message):
        self.logger.info(f"Виведення повідомлення: {message}")
        print(message)

    def choose_font_size(self):
        while True:
            try:
                print("Введіть розмір шрифту (наприклад, 2x2, 3x3 тощо):")
                font_size = input("Розмір шрифту: ")
                width_multiplier, height_multiplier = map(int, font_size.split('x'))
                return width_multiplier, height_multiplier
            except ValueError:
                print("Невірний формат розміру шрифту. Спробуйте ще раз.")

#lab4

        @staticmethod
        def get_input(prompt):
            """ Get input from the user. """
            return input(prompt)

        @staticmethod
        def print_message(message):
            """ Print a message to the user. """
            print(message)
