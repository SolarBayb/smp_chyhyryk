class HistoryManager:
    def __init__(self):
        self.history = []

    def add(self, expression, result):
        """Add a calculation and its result to the history."""
        self.history.append((expression, result))

    def view(self):
        """Display the calculation history."""
        if not self.history:
            print("Історії не знайдено.")
        else:
            for expr, res in self.history:
                print(f"{expr} = {res}")
