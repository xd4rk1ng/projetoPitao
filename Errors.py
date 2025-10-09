## Error classes

class Error:
    def __init__(self, message, exception):
        self.message = message
        self.exception = exception

    def __str__(self):
        return f"{self.message}"