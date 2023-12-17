from functions2 import Calculator

def run_calculator():
    calc = Calculator()
    while True:
        calc.get_input()
        while not calc.is_valid_operator():
            print("Недійсний оператор. Спробуйте ще раз.")
            calc.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        result = calc.safe_calculate()
        print(f"Результат: {result}")
        if not calc.repeat_calculation():
            break
