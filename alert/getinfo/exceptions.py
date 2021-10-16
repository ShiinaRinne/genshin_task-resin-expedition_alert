class APIError(ValueError):
    def __init__(self, retcode: int, message: str) -> None:
        self.retcode: int = retcode
        self.message: str = message

    def __str__(self) -> str:
        return f"{self.retcode}: {self.message}"
