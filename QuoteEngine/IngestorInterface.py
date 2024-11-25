"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

"""Module that declares abstract base class giving interface."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel, InvalidFileFormat
import os


class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestr classes for diffent types of files.

    Each child class will actually ingest the files and return desired data.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check whether this ingestor supports the input file."""
        _, ext = os.path.splitext(path)
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse the input file, checking whether it's supported first."""
        if not cls.can_ingest(path):
            raise InvalidFileFormat(path, cls)
        return cls._parse(path)

    @classmethod
    @abstractmethod
    def _parse(cls, path) -> List[QuoteModel]:
        """Format-specific parsing logic goes here."""
        raise NotImplementedError
