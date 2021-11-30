from utils import read_image
import pandas as pd


def hist(input_img, output_img):
    image, x, y = read_image(input_img)
    pixels = []
    for i in range(x):
        for j in range(y):
            pixel = image.getpixel((i, j))
            pixels.append((pixel))

    pixels = pd.Series(pixels)
    proportitionDict = dict(pixels.value_counts(normalize=True))

    hist_dict = {}
    add = 0
    for i in range(256):
        if i in proportitionDict.keys():
            add += proportitionDict[i]
        hist_dict[i] = add

    table = []
    for i in range(256):
        table.append(hist_dict[i] * 255)
    print(table)
    image = image.point(table, 'L')
    image.show()
    image.save(output_img)


if __name__ == "__main__":
    input_image = '../data/e.png'
    output_image = '../result/hist/hist.png'
    hist(input_image, output_image)
