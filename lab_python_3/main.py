from console import Console
from functions import ASCIIArtGenerator
#from Scripts.all_python_labs.shared_lib.console_ui import ConsoleUI
#from Scripts.all_python_labs.shared_lib.input_validator import InputValidator

def main():
    console = Console()
    art_generator = ASCIIArtGenerator()

    while True:
        text = console.get_input("Введіть слово або фразу для перетворення у ASCII ART: ")

        if art_generator.contains_ukrainian(text):
            console.print_message("Будь ласка, змініть розкладку та введіть текст англійською.")
            continue

        font = console.choose_option(art_generator.available_fonts(), "Виберіть номер шрифту: ")
        color = console.choose_option(art_generator.available_colors(), "Виберіть номер кольору: ")
        width_multiplier, height_multiplier = console.choose_font_size()

        ascii_art = art_generator.generate(text, font)
        resized_art = art_generator.resize(ascii_art, width_multiplier, height_multiplier)
        colored_art = art_generator.colorize(resized_art, color)

        console.print_colored_text(colored_art, color)

        preview = console.get_input("Зберегти цей ASCII ART? (y/n) ")
        if preview.lower() == 'y':
            art_generator.save(resized_art)
            console.print_message("ASCII ART збережений у файлі 'ascii_art.txt'")

        cont = console.get_input("Хочете спробувати ще раз? (y/n) ")
        if cont.lower() != 'y':
            break

# from Scripts.all_python_labs.shared_lib.runnable import Runnable
#
# def run(self):
#     """
#     Run the main application loop.
#
#     Returns:
#     - None
#     """
#     # Run the main application event loop
#     self.root.mainloop()
#
# def main():
#     console_ui = ConsoleUI()
#     art_generator = InputValidator()
#
#     while True:
#         text = console_ui.get_input("Введіть слово або фразу для перетворення у ASCII ART: ")
#
#         if art_generator.contains_ukrainian(text):
#             console_ui.display_message("Будь ласка, змініть розкладку та введіть текст англійською.")
#             continue
#
#         font = console_ui.choose_option(art_generator.available_fonts(), "Виберіть номер шрифту: ")
#         color = console_ui.choose_option(art_generator.available_colors(), "Виберіть номер кольору: ")
#         width_multiplier, height_multiplier = console_ui.choose_font_size()
#
#         ascii_art = art_generator.generate(text, font)
#         resized_art = art_generator.resize(ascii_art, width_multiplier, height_multiplier)
#         colored_art = art_generator.colorize(resized_art, color)
#
#         console_ui.print_colored_text(colored_art, color)
#
#         preview = console_ui.get_input("Зберегти цей ASCII ART? (y/n) ")
#         if preview.lower() == 'y':
#             art_generator.save(resized_art)
#             console_ui.display_message("ASCII ART збережений у файлі 'ascii_art.txt'")
#
#         cont = console_ui.get_input("Хочете спробувати ще раз? (y/n) ")
#         if cont.lower() != 'y':
#             break

if __name__ == "__main__":
    main()
