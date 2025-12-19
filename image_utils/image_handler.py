from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGB")  
        self.path = image_path

    def resize(self, width, height):
        self.image = self.image.resize((width, height), Image.LANCZOS)

    def save(self, output_path):
        self.image.save(output_path, "PNG")

    def get_image(self):
        return self.image.copy()  

    def set_image(self, new_image):
        self.image = new_image.copy()  