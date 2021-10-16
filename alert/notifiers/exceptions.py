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