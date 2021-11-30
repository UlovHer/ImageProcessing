from PIL import Image


def read_image(img_path):
    image = Image.open(img_path)
    image = image.convert('L')
    x = image.size[0]
    y = image.size[1]
    return image, x, y
