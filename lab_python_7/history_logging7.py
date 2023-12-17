import datetime

class HistoryLogger:
    LOG_FILE = 'history_log7.txt'

    @staticmethod
    def log_history(user_input, result):
        """Log user input and result to a file."""
        with open(HistoryLogger.LOG_FILE, 'a', encoding='utf-8') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - Input: {user_input}, Result: {result}\n"
            file.write(log_entry)

    @staticmethod
    def read_history():
        """Read and return the history from the log file."""
        try:
            with open(HistoryLogger.LOG_FILE, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "History not found."
