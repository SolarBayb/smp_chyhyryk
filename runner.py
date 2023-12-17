import subprocess
import sys

def run_lab(lab_number):
    try:
        if lab_number == 3:
            # Особливий випадок для лабораторної роботи 3
            subprocess.run([sys.executable, f"lab_python_3/main.py"])
        else:
            # Загальний випадок для інших лабораторних робіт
            subprocess.run([sys.executable, f"lab_python_{lab_number}/main{lab_number}.py"])
    except Exception as e:
        print(f"Помилка при запуску лабораторної роботи {lab_number}: {e}")

def generate_pydoc(lab_number, output_format='text'):
    module_path = f"lab_python_{lab_number}/main{lab_number}.py"
    try:
        if output_format == 'html':
            subprocess.run(['pydoc', '-w', module_path])
        else:
            subprocess.run(['pydoc', module_path])
    except Exception as e:
        print(f"Помилка при генерації документації для лабораторної роботи {lab_number}: {e}")

def main():
    while True:
        print("\nОпції:")
        print("1. Запустити лабораторні роботи")
        print("2. Генерувати документацію")

        main_choice = input("\nВиберіть опцію (або 'exit' для виходу): ")

        if main_choice.lower() == 'exit':
            break

        if main_choice == '1':
            print("\nЛабораторні роботи:")
            for i in [1, 2, 3, 4, 5, 7, 8]:
                print(f"{i}. Лабораторна робота {i}")

            lab_choice = input("\nВведіть номер лабораторної роботи для запуску: ")
            if lab_choice.isdigit() and int(lab_choice) in [1, 2, 3, 4, 5, 7, 8]:
                run_lab(int(lab_choice))
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        elif main_choice == '2':
            print("\nГенерація документації для лабораторних робіт:")
            for i in [1, 2, 3, 4, 5, 7, 8]:
                print(f"{i}. Лабораторна робота {i}")

            lab_choice = input("\nВведіть номер лабораторної роботи для генерації документації: ")
            if lab_choice.isdigit() and int(lab_choice) in [1, 2, 3, 4, 5, 7, 8]:
                doc_format = input("Виберіть формат документації ('text' або 'html'): ")
                generate_pydoc(int(lab_choice), output_format=doc_format)
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
