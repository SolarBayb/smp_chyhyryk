from api_client7 import APIClient
from console7 import ConsOleUI
# from Scripts.all_python_labs.shared_lib.calculation_functions import CalculationFunctions
# from Scripts.all_python_labs.shared_lib.memory_manager import MemoryManager
# from Scripts.all_python_labs.shared_lib.history_logger import HistoryLogger
# from Scripts.all_python_labs.shared_lib.data_manager import DataManager
# from Scripts.all_python_labs.shared_lib.input_validator import InputValidator
from history_logging7 import HistoryLogger
from input_parser7 import InputValidator


def main():
    api_client = APIClient()
    console_ui = ConsOleUI(api_client)
    input_validator = InputValidator()
    history_logger = HistoryLogger()

    while True:
        choice = console_ui.display_menu()

        if choice == '1':
            date_input = ''
            while not input_validator.validate_date(date_input):
                date_input = input("Enter date (DD-MM-YYYY): ")
                if not input_validator.validate_date(date_input):
                    print("Invalid date format. Try again.")

            phone_input = ''
            while not input_validator.validate_phone_number(phone_input):
                phone_input = input("Enter phone number: ")
                if not input_validator.validate_phone_number(phone_input):
                    print("Invalid phone number format. Try again.")

            display_format = ''
            while not input_validator.validate_display_format(display_format):
                display_format = console_ui.choose_display_format()
                if not input_validator.validate_display_format(display_format):
                    print("Invalid display format. Try again.")

            num_posts_str = ''
            num_posts = 0
            while not num_posts:
                num_posts_str = console_ui.choose_number_of_posts()
                num_posts = input_validator.validate_number(num_posts_str)
                if not num_posts:
                    print("Invalid number of posts. Enter a positive integer.")

            posts = api_client.get_posts()
            color_choice = console_ui.choose_color()
            color_code = console_ui.get_color_code(color_choice)

            if display_format == '2':  # Table format
                style_choice = console_ui.choose_table_style()
                console_ui.display_posts(posts, display_format, num_posts, color_code, style_choice)
            else:  # List format
                list_style_choice = console_ui.choose_list_style()
                console_ui.display_list(posts, num_posts, color_code, list_style_choice)

            ask_to_save = console_ui.ask_to_save_data(posts)
            if ask_to_save:
                history_logger.log_history("Saved posts", "Success")

        elif choice == '2':
            print("Exiting the program...")
            break

        elif choice == '3':
            print("Request History:")
            print(history_logger.read_history())

        else:
            print("Unknown command, try again.")


if __name__ == "__main__":
    main()

