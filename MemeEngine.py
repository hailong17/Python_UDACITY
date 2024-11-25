"""
Project: Meme Generator
Author: LongNH63
Date: 24/11/2024
"""

from Exceptions import InvalidFilePath
from Exceptions import exception
from PIL import Image, ImageFont, ImageDraw
import random

import Exceptions


class MemeEngine:
    """Class to generate actual meme file."""

    def __init__(self, path):
        """Initialize the MemeEngine."""
        self.temp_dir = path

    def make_meme(self, img_path: str,
                  text: str, author: str,
                  width=500) -> str:
        """Gernerate Meme with given img, text, and author."""
        width = min(width, 1000)
        out_path = f"{self.temp_dir}/{random.randint(0,1000)}.png"
        default_font = "./_data/arial.ttf"
        default_font_size = 30

        if width >= 500:
            width = 500
        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = int(width * ratio)
                img = img.resize((int(width), int(height)))
                default_font_size = int(img.height/20)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(default_font, default_font_size)

                text_x = random.randint(0, int(img.width/4))
                text_y = random.randint(0, int(img.height-default_font_size*2))

                draw.text((text_x, text_y), text, font=font, fill="black")
                draw.text((int(text_x*1.2), text_y+default_font_size), " - "+author, font=font)
                img.save(out_path)

        except Exception:
            raise InvalidFilePath("Invalid image path")

        return out_path
