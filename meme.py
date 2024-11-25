"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

import os
import random
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./output')
    path = meme.make_meme(img, quote.body, quote.author)
    return path

def parse_arguments():
    """ Parse arguments. """
    parser = argparse.ArgumentParser(description='Generate meme!!')
    parser.add_argument('--body', type=str, default=None, help="text that want to show")
    parser.add_argument('--author', type=str, default=None, help="author of the text")
    parser.add_argument('--path', type=str, default=None, help="file path for background image you want")
    return parser.parse_args()

def main():
    """ Run. """
    args = parse_arguments()
    meme = generate_meme(args.path, args.body, args.author)
    print("Meme generated in at '{}'".format(meme))

if __name__ == "__main__":
    main()
