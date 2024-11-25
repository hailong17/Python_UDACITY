"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxImporter(IngestorInterface):
    """Helper module to read Docx file."""

    allowed_extensions = ".docx"

    @classmethod
    def parse(cls, path: str):
        """Parse docx file using pandas library

        Args:
            path (str): path to the docx file

        Returns:
            quotes (List[QuoteModel]): list of QuoteModel
        """
        if not cls.can_ingest(path):
            raise ValueError("Cannot ingest the provided file.")

        quotes = []

        try:
            doc = docx.Document(path)
        except Exception as e:
            raise ValueError(f"Error reading the .docx file: {e}")

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body = parse[0].strip().strip('"')
                author = parse[1].strip()
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
