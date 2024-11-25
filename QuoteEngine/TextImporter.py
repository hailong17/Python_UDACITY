"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Parse text file

        Args:
            path (str): path to the text file

        Returns:
            quotes (List[QuoteModel]): list of QuoteModel
        """

    allowed_extensions = '.txt'

    @classmethod
    def parse(cls, path: str):
        """Parse txt file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        with open(path, 'r') as f:
            for line in f:
                if "-" not in line:
                    continue
            try:
                body = line.split("-")[0].strip().strip('"')
                author = line.split("-")[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
            except IndexError:
                    print(f"Warning: Skipping malformed line: {line.strip()}")

        return quotes
