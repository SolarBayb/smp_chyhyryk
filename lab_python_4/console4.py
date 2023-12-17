class Console:
    output_color = 'default'

    @staticmethod
    def get_input(prompt):
        """ Get input from the user with error checking. """
        while True:
            user_input = input(prompt)
            if Console._is_input_valid(user_input):
                return user_input
            else:
                Console.print_message("Input error detected. Do you want to rewrite? (yes/no): ")
                if input().strip().lower() != 'yes':
                    return None

    @staticmethod
    def print_message(message):
        """ Print a message to the user with the chosen color and symbol. """
        color_start = Console._get_color_code(Console.output_color)
        color_end = Console._get_color_code('end')
        print(f"{color_start} {message}{color_end}")

    @staticmethod
    def set_output_color(color):
        """ Set the color of the output text. """
        Console.output_color = color


    @staticmethod
    def _get_color_code(color):
        """ Get the ANSI color code for the given color. """
        colors = {
            'default': '',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'end': '\033[0m'
        }
        return colors.get(color, '')

    @staticmethod
    def _is_input_valid(user_input):
        """ Check if the user input is valid (not empty or just whitespace). """
        return user_input.strip() != ''

# Example usage
Console.set_output_color('blue')


