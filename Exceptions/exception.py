class CustomException(Exception):
    """Base class for custom exceptions."""
    pass


class InvalidFileFormat(CustomException):
    """Raised when the file format is invalid."""
    pass


class InvalidTextInput(CustomException):
    """Raised when the text input is invalid."""
    pass


class InvalidFilePath(CustomException):
    """Raised when the file path is invalid or does not exist."""
    pass
