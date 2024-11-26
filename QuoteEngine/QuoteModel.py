"""Module for QuoteModel Class."""

from dataclasses import dataclass


@dataclass(frozen=True)
class QuoteModel:
    """Represent models for Quote."""

    body: str
    author: str

    def __str__(self):
        """Return the string representation."""
        return f'"{self.body}" - {self.author}'


class InvalidFileFormat(Exception):
    def __init__(self, path: str, cls: type):
        self.path = path
        self.cls = cls
        super().__init__(f"Invalid file format for '{path}'. {cls.__name__}\
                         cannot ingest this file.")
