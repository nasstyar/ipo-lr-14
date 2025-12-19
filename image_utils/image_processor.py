from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def add_text(self, text, position="bottom_right", font_size=20):
        draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        w, h = self.image.size

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        if position == "bottom_right":
            x = w - text_width - 10
            y = h - text_height - 10
        else:
            x, y = 10, 10 

        draw.text((x, y), text, fill="white", font=font, stroke_width=1, stroke_fill="black")