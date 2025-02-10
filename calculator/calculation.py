class Calculations:
    """Encapsulates a single calculation."""
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        # call
        return self.operation(self.a, self.b)
