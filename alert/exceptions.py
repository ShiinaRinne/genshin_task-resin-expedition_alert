class APIError(ValueError):
    def __init__(self, retcode: int, message: str) -> None:
        self.retcode: int = retcode
        self.message: str = message

    def __str__(self) -> str:
        return f"{self.retcode}: {self.message}"

class AlertException(Exception):
    """Base genshinhelper exception."""

    def __init__(self, message):
        super().__init__(message)
        print(message)

class CookiesExpired(AlertException):
    """Cookies has expired."""


class NotificationError(AlertException):
    """
    A notification error. Raised after an issue with the sent notification.
    """


class NoSuchNotifierError(AlertException):
    """
    An unknown notifier was requests, one that was not registered.
    """