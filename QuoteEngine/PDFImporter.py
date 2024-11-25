"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random
import os


class PDFImporter(IngestorInterface):
    """Parse pdf file

        Args:
            path (str): path to the pdf file

        Returns:
            quotes (List[QuoteModel]): list of QuoteModel
        """

    allowed_extensions = '.pdf'

    @classmethod
    def parse(cls, path: str):
        """Parse pdf file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception('Connot Ingest Exception')

        quotes = []

        output = f'./output/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, output])
        file_ref = open(output, "r")
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0].strip().strip('"'), parsed[1].strip())
                quotes.append(new_quote)

        file_ref.close()
        os.remove(output)

        return quotes
