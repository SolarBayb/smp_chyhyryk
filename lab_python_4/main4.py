# from Scripts.all_python_labs.shared_lib.input_validator import InputValidator
# from Scripts.all_python_labs.shared_lib.console_ui import ConsoleUI
from ascii_art_generator4 import ASCIIArtGenerator
from console4 import Console
from alphabet4 import Alphabet  # Assuming the updated Alphabet class is in a file named alphabet4.py

def main():
    console = Console()

    # Setting up the ASCII Art Generator
    language = 'english'
    art_generator = ASCIIArtGenerator(language=language)

    while True:
        # Customizing output color and symbol
        output_color = console.get_input("Choose an output color (default, red, green, etc.): ")
        console.set_output_color(output_color)

        # Getting text input for ASCII art
        text = console.get_input("Enter a word or phrase for ASCII art: ")

        # Checking for language constraints
        if language == 'ukrainian' and art_generator.contains_ukrainian(text):
            console.print_message("Please enter text in Ukrainian.")
            continue

        # Generating ASCII art
        ascii_art = art_generator.generate(text)
        console.print_message(ascii_art)

        # Option to save ASCII art
        save = console.get_input("Save this ASCII ART? (y/n): ").lower() == 'y'
        if save:
            art_generator.save(ascii_art)
            console.print_message("ASCII art saved in 'ascii_art.txt'.")

        # Option to try again or exit
        if console.get_input("Try again? (y/n): ").lower() != 'y':
            break

# def main():
#     console_ui = ConsoleUI()
#     language = 'english'
#
#     art_generator = ASCIIArtGenerator(language=language)
#
#     while True:
#         text = console_ui.get_input("Enter a word or phrase for ASCII art: ")
#
#         if language == 'ukrainian' and art_generator.contains_ukrainian(text):
#             console_ui.print_message("Please enter text in Ukrainian.")
#             continue
#
#         ascii_art = art_generator.generate(text)
#         console_ui.print_message(ascii_art)
#
#         save = console_ui.get_input("Save this ASCII ART? (y/n): ").lower() == 'y'
#         if save:
#             art_generator.save(ascii_art)
#             console_ui.print_message("ASCII art saved in 'ascii_art.txt'.")
#
#         if console_ui.get_input("Try again? (y/n): ").lower() != 'y':
#             break
#
if __name__ == "__main__":
    main()
