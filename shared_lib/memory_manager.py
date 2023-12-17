import logging

class MemoryManager:
    def __init__(self):
        self.memory = None

    def store(self, value):
        """Store a value in memory."""
        self.memory = value
        logging.info(f"Value stored in memory: {value}")

    def retrieve(self):
        """Retrieve the stored value from memory."""
        if self.memory is not None:
            logging.info(f"Retrieved value from memory: {self.memory}")
            return self.memory
        else:
            logging.warning("Attempted to retrieve value, but memory is empty")
            return "В пам'яті немає значень"
