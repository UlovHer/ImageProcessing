from utils import read_image


def normal(input_img, output_img):
    image, x, y = read_image(input_img)
    pixels = []
    for i in range(x):
        for j in range(y):
            pixel = image.getpixel((i, j))
            pixels.append((pixel))
    pixel_max = max(pixels)
    pixel_min = min(pixels)

    table = []
    for i in range(256):
        table.append(200 * (i - pixel_min) / (pixel_max - pixel_min))
    image = image.point(table, 'L')
    image.show()
    image.save(output_img)


if __name__ == "__main__":
    input_image = '../data/d.png'
    output_image = '../result/normal/normal_image.png'
    normal(input_image, output_image)
