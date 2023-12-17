import re
from datetime import datetime

class InputValidator:
    @staticmethod
    def validate_number(input_str):
        """Checks if the input string is a positive integer."""
        try:
            number = int(input_str)
            if number > 0:
                return number
            else:
                raise ValueError("The number must be greater than 0.")
        except ValueError:
            return None

    @staticmethod
    def validate_display_format(input_str):
        """Checks if the input display format is valid (either '1' or '2')."""
        if input_str in ['1', '2']:
            return input_str
        else:
            return None

    @staticmethod
    def validate_date(input_str):
        """Checks if the input is a valid date in the format DD-MM-YYYY."""
        try:
            datetime.strptime(input_str, '%d-%m-%Y')
            return input_str
        except ValueError:
            return None

    @staticmethod
    def validate_phone_number(input_str):
        """Checks if the input is a valid phone number."""
        pattern = r'(\+?\d{1,3}?[-.\s]?)?(\(?\d{2,3}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}'
        if re.match(pattern, input_str):
            return input_str
        else:
            return None
