import pyfiglet
from colorama import init, Fore

class ASCIIArtGenerator:
    def __init__(self):
        init(autoreset=True)

    @staticmethod
    def contains_ukrainian(text):
        return any(char in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" for char in text.lower())

    def available_fonts(self):
        return pyfiglet.FigletFont.getFonts()

    def available_colors(self):
        return ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def generate(self, text, font):
        return pyfiglet.figlet_format(text, font=font)

    def colorize(self, text, color):
        color_map = {
            'grey': Fore.LIGHTBLACK_EX,
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.LIGHTWHITE_EX
        }
        return color_map[color] + text

    def save(self, ascii_art):
        with open('ascii_art.txt', 'w') as file:
            file.write(ascii_art)

    @staticmethod
    def resize(ascii_art, width_multiplier, height_multiplier):
        lines = ascii_art.split("\n")
        new_lines = []

        for line in lines:
            new_line = "".join([char * width_multiplier for char in line])
            for _ in range(height_multiplier):
                new_lines.append(new_line)

        return "\n".join(new_lines)
