from functions1 import get_input, is_valid_operator, Calculator, safe_calculate
from memory_manager1 import MemoryManager
from history_manager1 import HistoryManager

def choose_task():
    """Дозволяє користувачеві вибрати завдання для виконання."""
    calculator = Calculator()
    memory_manager = MemoryManager()
    history_manager = HistoryManager()

    while True:
        print("\nВиберіть завдання для виконання:")
        print("1: Введення користувача і обчислення")
        print("2: Перевірка історії обчислень")
        print("3: Отримання значення з пам'яті")
        print("4: Вихід з програми")

        choice = input("Ваш вибір: ")

        if choice == "1":
            num1, num2, operator = get_input()
            while not is_valid_operator(operator):
                print("Недійсний оператор. Спробуйте ще раз.")
                operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            result = safe_calculate(num1, num2, operator)
            print(f"Результат: {result}")
            history_manager.add(f"{num1} {operator} {num2}", result)
            memory_manager.store(result)

        elif choice == "2":
            history_manager.view()

        elif choice == "3":
            value = memory_manager.retrieve()
            print(f"Значення у пам'яті: {value}")

        elif choice == "4":
            print("Вихід з програми.")
            break

        else:
            print("Невідомий вибір. Спробуйте ще раз.")
