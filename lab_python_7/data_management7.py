import json

class DataManager:
    @staticmethod
    def save_data_to_file(data, filename='data.txt'):
        """Saves data to a specified file in JSON format."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {filename}.")

    @staticmethod
    def load_data_from_file(filename='data.txt'):
        """Loads data from a specified file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")
            return None
