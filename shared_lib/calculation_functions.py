import logging

class CalculationFunctions:

#lab1

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = ""
        self.valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Додавання обробника логування
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def get_input(self):
        self.logger.info("Запит введення від користувача")
        """Отримання введення від користувача."""
        self.num1 = self._get_number("Введіть перше число: ")
        self.num2 = self._get_number("Введіть друге число: ")
        self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

    def _get_number(self, prompt):
        """Отримує число від користувача."""
        while True:
            try:
                value = input(prompt)
                return float(value)
            except ValueError:
                print("Неправильна умова, введіть число ще раз.")

    def is_valid_operator(self):
        """Перевірка чи оператор є дійсним."""
        return self.operator in self.valid_operators


    def calculate(self):
        self.logger.info(f"Обчислення {self.num1} {self.operator} {self.num2}")
        """Виконання обчислень на основі введення користувача."""
        if self.operator not in self.valid_operators:
            raise ValueError("Недійсний оператор")
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 == 0:
                raise ZeroDivisionError("Помилка: ділення на нуль!")
            return self.num1 / self.num2
        elif self.operator == '^':
            return self.num1 ** self.num2
        elif self.operator == '√':
            if self.num1 < 0:
                raise ValueError("Корінь з від'ємного числа не дозволений")
            return self.num1 ** (1 / self.num2)
        elif self.operator == '%':
            return self.num1 % self.num2

    def safe_calculate(self):
        self.logger.info("Безпечне обчислення")
        """Безпечне виконання обчислень з обробкою помилок."""
        try:
            return self.calculate()
        except (ZeroDivisionError, ValueError, Exception) as e:
            return f"Помилка: {e}"

    def repeat_calculation(self):
        self.logger.info("Запит на повторення обчислення")
        """Запитує, чи користувач хоче повторити обчислення."""
        while True:
            repeat = input("Чи хочете ви виконати ще одне обчислення? (так/ні): ").lower()
            if repeat == "так":
                return True
            elif repeat == "ні":
                return False
            else:
                print("Помилка: неправильний текст. Введіть 'так' або 'ні'.")

#lab2

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = ""
        self.valid_operators = ['+', '-', '*', '/', '^', '√', '%']


    def get_input(self):
        while True:
            try:
                value = input("Введіть перше число: ")
                if not value.replace('.', '', 1).isdigit():
                    raise ValueError
                self.num1 = float(value)
                break
            except ValueError:
                print("Неправильна умова, введіть число ще раз.")

        while True:
            try:
                value = input("Введіть друге число: ")
                if not value.replace('.', '', 1).isdigit():
                    raise ValueError
                self.num2 = float(value)
                break
            except ValueError:
                print("Неправильна умова, введіть число ще раз.")

        self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")


    def is_valid_operator(self):
        return self.operator in self.valid_operators


    def calculate(self):
        if self.operator not in self.valid_operators:
            raise ValueError("Недійсний оператор")
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 == 0:
                raise ZeroDivisionError("Помилка: ділення на нуль!")
            return self.num1 / self.num2
        elif self.operator == '^':
            return self.num1 ** self.num2
        elif self.operator == '√':
            if self.num1 < 0:
                raise ValueError("Корінь з від'ємного числа не дозволений")
            return self.num1 ** (1 / self.num2)
        elif self.operator == '%':
            return self.num1 % self.num2


    def safe_calculate(self):
        try:
            return self.calculate()
        except ZeroDivisionError as e:
            return f"Помилка: {e}"
        except ValueError as e:
            return f"Помилка: {e}"
        except Exception as e:
            return f"Помилка: {e}"


    def repeat_calculation(self):
        while True:
            repeat = input("Чи хочете ви виконати ще одне обчислення? (так/ні): ").lower()
            if repeat == "так":
                return True
            elif repeat == "ні":
                exit()
            else:
                print("Помилка: неправильний текст. Введіть 'так' або 'ні'.")
