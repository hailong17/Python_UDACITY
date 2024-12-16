"""Text Importer."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextImporter(IngestorInterface):
    """Parse text file."""

    allowed_extensions = '.txt'

    @classmethod
    def parse(cls, path: str):
        """Parse txt file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception: Unsupported file type')

        quotes = []

        try:
            with open(path, 'r') as f:
                for line in f:
                    if "-" not in line:
                        continue
                try:
                    body = line.split("-")[0].strip().strip('"')
                    author = line.split("-")[1].strip()
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)
                except ValueError as e:
                    print(f"Warning: Skipping malformed line:\
                          {line.strip()} | Error: {e}")
        except FileNotFoundError:
            print(f"Error: File not found - {path}")

        return quotes
