import datetime
import logging

class HistoryLogger:
    def __init__(self):
        self.history = []

        # Налаштування логера
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler('history_logger.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def add(self, expression, result):
        """Add a calculation and its result to the history."""
        self.history.append((expression, result))
        self.logger.info(f"Added to history: {expression} = {result}")

    def view(self):
        """Display the calculation history."""
        if not self.history:
            print("Історії не знайдено.")
            self.logger.warning("History is empty.")
        else:
            for expr, res in self.history:
                print(f"{expr} = {res}")
#lab7

    LOG_FILE = 'history_log7.txt'

    @staticmethod
    def log_history(user_input, result):
        """Log user input and result to a file."""
        with open(HistoryLogger.LOG_FILE, 'a', encoding='utf-8') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - Input: {user_input}, Result: {result}\n"
            file.write(log_entry)
        logging.info(f"Logged to file: Input: {user_input}, Result: {result}")

    @staticmethod
    def read_history():
        """Read and return the history from the log file."""
        try:
            with open(HistoryLogger.LOG_FILE, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logging.error("History log file not found.")
            return "History not found."