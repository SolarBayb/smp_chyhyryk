class MemoryManager:
    def __init__(self):
        self.memory = None

    def store(self, value):
        """Store a value in memory."""
        self.memory = value

    def retrieve(self):
        """Retrieve the stored value from memory."""
        if self.memory is not None:
            return self.memory
        else:
            return "В пам'яті немає значень"
