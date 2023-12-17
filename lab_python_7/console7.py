from prettytable import PrettyTable
from data_management7 import DataManager
from input_parser7 import InputValidator
# from Scripts.all_python_labs.shared_lib.calculation_functions import CalculationFunctions
# from Scripts.all_python_labs.shared_lib.memory_manager import MemoryManager
# from Scripts.all_python_labs.shared_lib.history_logger import HistoryLogger
# from Scripts.all_python_labs.shared_lib.api_client import APIClient
# from Scripts.all_python_labs.shared_lib.data_manager import DataManager
# from Scripts.all_python_labs.shared_lib.input_validator import InputValidator
from prettytable import PrettyTable


class ConsOleUI:
    def __init__(self, api_client):
        self.api_client = api_client

    def display_menu(self):
        print("1: Retrieve Posts")
        print("2: Exit")
        print("3: View History")
        return input("Your choice: ")

    def choose_display_format(self):
        print("Select display format:")
        print("1: List")
        print("2: Table")
        return input("Your choice (1/2): ")

    def choose_number_of_posts(self):
        return input("Enter the number of posts to display: ")

    def choose_table_style(self):
        print("Select table style:")
        print("1: Plain")
        print("2: Line-separated")
        return input("Your choice (1/2): ")

    def choose_list_style(self):
        print("Select list style:")
        print("1: Plain")
        print("2: Numbered")
        return input("Your choice (1/2): ")

    def ask_to_save_data(self, data):
        user_choice = input("Do you want to save the data to a file? (yes/no): ").lower()
        if user_choice in ['yes', 'так']:
            filename = input("Enter file name (default: data.txt): ")
            filename = filename if filename else 'data.txt'
            DataManager.save_data_to_file(data, filename)
            print(f"Data saved to file: {filename}")
        else:
            print("Save cancelled.")

    def choose_color(self):
        print("Choose a color:")
        print("1: Gray")
        print("2: Red")
        print("3: Green")
        print("4: Yellow")
        print("5: Blue")
        print("6: Pink")
        print("7: Cyan")
        print("8: White")
        return input("Your choice (1-8): ")

    def get_color_code(self, color_choice):
        colors = {
            '1': '\033[30m',  # Gray
            '2': '\033[31m',  # Red
            '3': '\033[32m',  # Green
            '4': '\033[33m',  # Yellow
            '5': '\033[34m',  # Blue
            '6': '\033[35m',  # Pink
            '7': '\033[36m',  # Cyan
            '8': '\033[37m',  # White
        }
        return colors.get(color_choice, '\033[0m')  # Default color

    def display_list(self, posts, num_posts, color_code, list_style_choice):
        num_posts = int(num_posts)
        posts = posts[:num_posts]

        for index, post in enumerate(posts, start=1):
            if list_style_choice == '2':  # Numbered list
                print(f"{color_code}{index}. ID: {post['id']}, Title: {post['title']}\033[0m")
            else:  # Plain list
                print(f"{color_code}ID: {post['id']}, Title: {post['title']}\033[0m")

    def display_posts(self, posts, display_format, num_posts, color_code, table_style_choice):
        num_posts = int(num_posts)
        posts = posts[:num_posts]

        if display_format == '2':  # Table format
            table = PrettyTable()
            table.field_names = [f"{color_code}ID\033[0m", f"{color_code}Title\033[0m"]

            for post in posts:
                table.add_row([post['id'], post['title']])

            if table_style_choice == '2':  # Style with lines
                table.border = True
                table.header = True
                table.horizontal_char = '-'
                table.vertical_char = '|'
                table.junction_char = '+'
            else:  # Default style
                table.border = False
                table.header = True
                table.horizontal_char = ' '
                table.vertical_char = ' '
                table.junction_char = ' '

            print(table)
        else:  # List format
            self.display_list(posts, num_posts, color_code, table_style_choice)
