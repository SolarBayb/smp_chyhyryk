from Scripts.all_python_labs.lab_python_4.alphabet4 import get_ascii_art

from Scripts.all_python_labs.lab_python_4 import *
class ASCIIArtGenerator:
    def __init__(self, language='english'):
        self.language = language

    def generate(self, text):
        lines = ['' for _ in range(5)]  # Припускаємо 5 рядків на літеру
        for char in text:
            char_art = get_ascii_art(char, self.language)
            if char_art:
                for i, line in enumerate(char_art):
                    lines[i] += line + "  "  # Додаємо пробіл між символами
            else:
                # Якщо символ не знайдено, повертаємо повідомлення про це
                return f"Символ '{char}' не знайдено в ASCII арт представленнях."
        return "\n".join(lines)

    def save(self, ascii_art, filename='ascii_art.txt'):
        """Saves ASCII art to a file."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(ascii_art)
            return True
        except Exception as e:
            print(f"Error saving ASCII art: {e}")
            return False