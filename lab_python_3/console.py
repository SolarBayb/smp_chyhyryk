class Console:

    @staticmethod
    def get_input(prompt):
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
