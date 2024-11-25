"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    imgs = []
    images_path = "./_data/photos/dog/"

    for quote_file in quote_files:
        try:
            print(f"Processing: {quote_file}")
            quotes += Ingestor.parse(quote_file)
            print(Ingestor.parse(quote_file))
        except Exception as e:
            print(f"Error processing file {quote_file}: {e}")

    try:
        for file in os.listdir(images_path):
            if file.endswith(".jpg"):
                imgs.append(os.path.join(images_path, file))
    except Exception as e:
        print(f"Error reading image files from {images_path}: {e}")

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    if not request.form["image_url"]:
        return render_template('meme_form.html')

    image_url = request.form["image_url"]
    try:
        r = requests.get(image_url, verify=False)
        r.raise_for_status()
        output = f'./output/{random.randint(0,1000)}.png'
        with open(output, 'wb') as img_file:
            img_file.write(r.content)

    except requests.exceptions.RequestException as e:
        # Catch any issues with the HTTP request
        print(f"Error fetching the image URL: {e}")
        return render_template('meme_form.html', error="Invalid image URL or network issue.")

    body = request.form["body"]
    author = request.form["author"]
    try:
        path = meme.make_meme(output, body, author)
    except Exception as e:
        print(f"Error creating the meme: {e}")

    os.remove(output)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
