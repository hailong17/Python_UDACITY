"""CSV Importer."""
"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd


class CSVImporter(IngestorInterface):
    """Helper module to read CSV file."""

    allowed_extensions = ".csv"

    @classmethod
    def parse(cls, path: str):
        """Parse csv file using pandas library."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception: Unsupported file type')

        # Read CSV file and check neccessary column
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise ValueError(f"Error reading the file: {e}")

        if 'body' not in df.columns or 'author' not in df.columns:
            raise ValueError("CSV file must contain \
                             'body' and 'author' columns")

        # Creata QuoteModel list by list comprehension
        quotes = [
            QuoteModel(row['body'], row['author'])
            for _, row in df.iterrows()
            if pd.notnull(row['body']) and pd.notnull(row['author'])
        ]

        return quotes
