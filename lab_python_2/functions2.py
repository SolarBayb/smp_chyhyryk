class Calculator:
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
            return self.num1 ** (1/self.num2)
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
