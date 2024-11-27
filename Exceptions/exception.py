"""My custom Exception."""
class CustomException(Exception):
    """Base class for custom exceptions."""

    pass

"""Invalid Format."""
class InvalidFileFormat(CustomException):
    """Raised when the file format is invalid."""

    pass

"""Invalid Input."""
class InvalidTextInput(CustomException):
    """Raised when the text input is invalid."""

    pass

"""Invalid File Path."""
class InvalidFilePath(CustomException):
    """Raised when the file path is invalid or does not exist."""

    pass
