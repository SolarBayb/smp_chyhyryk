import json
import pandas as pd
import matplotlib.pyplot as plt
import logging

class DataManager:
    def __init__(self, csv_file=None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        if csv_file:
            self.data = self.load_data(csv_file)
        else:
            self.data = None

    @staticmethod
    def save_data_to_file(data, filename):
        """Зберігає дані у файл у форматі JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data successfully saved to {filename}.")
        except Exception as e:
            logging.error(f"Error saving data to file {filename}: {e}")


    @staticmethod
    def load_data_from_file(filename):
        """Завантажує дані з файлу у форматі JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning(f"File {filename} not found.")
            return None
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from {filename}.")
            return None


#lab7

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

#lab8

    def __init__(self, csv_file=None):
        if csv_file:
            self.data = self.load_data(csv_file)
        else:
            self.data = None

    def load_data(self, csv_file):
        self.initialize_logger()
        try:
            self.data = pd.read_csv(csv_file)
            self.logger.info(f"Data loaded from {csv_file}.")
            return self.data
        except FileNotFoundError:
            self.logger.error(f"File not found: {csv_file}")
            self.data = None

    def initialize_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def explore_data(self):
        """Досліджує дані."""
        if self.data is not None:
            logging.info("Data exploration started.")
            return self.data.describe()
        else:
            logging.warning("Data not loaded for exploration.")
            return "No data to explore."

    def basic_visualization(self, column_name):
        """Створює базову візуалізацію для вказаної колонки."""
        if self.data is not None and column_name in self.data.columns:
            logging.info(f"Creating basic visualization for {column_name}.")
            self.data[column_name].hist()
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column_name}')
            plt.show()
        else:
            logging.warning(f"Column {column_name} not found for visualization.")

    def advanced_visualization(self, column_x, column_y):
        """Створює складну візуалізацію."""
        if self.data is not None and column_x in self.data.columns and column_y in self.data.columns:
            logging.info(f"Creating advanced visualization: {column_x} vs {column_y}.")
            plt.scatter(self.data[column_x], self.data[column_y])
            plt.xlabel(column_x)
            plt.ylabel(column_y)
            plt.title(f'Scatter plot: {column_x} vs {column_y}')
            plt.show()
        else:
            logging.warning("Columns for advanced visualization not found.")

    def multiple_subplots(self, columns):
        """Створює декілька піддіаграм."""
        if self.data is not None:
            logging.info("Creating multiple subplots.")
            fig, axs = plt.subplots(len(columns), figsize=(10, 5))
            for i, col in enumerate(columns):
                if col in self.data.columns:
                    axs[i].plot(self.data[col])
                    axs[i].set_title(col)
                else:
                    logging.warning(f"Column {col} not found for subplot.")
            plt.tight_layout()
            plt.show()
        else:
            logging.warning("Data not loaded for creating subplots.")

    def export_visualization(self, filename, file_format='png'):
        """Експортує останню візуалізацію у файл."""
        try:
            plt.savefig(f'{filename}.{file_format}')
            logging.info(f"Visualization exported to {filename}.{file_format}.")
        except Exception as e:
            logging.error(f"Error exporting visualization: {e}")