import numpy as np
import random
from utils import read_image
from PIL import Image
# 使用Python Imaging Library


def add_pepper_noise(img_path):
    """
    给图片添加椒盐噪声
    """
    image, x, y = read_image(img_path)
    for i in range(x):
        for j in range(y):
            pixel = image.getpixel((i, j))
            if random.random() > 0.99:
                image.putpixel((i, j), 255 if random.random() > 0.5 else 0)
            else:
                image.putpixel((i, j), pixel)
    return image


def add_gaussian_noise(img_path):
    """
    给图片添加高斯噪声
    """
    image, x, y = read_image(img_path)
    gaussian_noise = 30 * np.random.normal(0, 1, (x, y))
    for i in range(x):
        for j in range(y):
            pixel = image.getpixel((i, j))
            if random.random() > 0.99:
                new_pixel = int(gaussian_noise[i, j] + pixel)
                image.putpixel((i, j), new_pixel)
            else:
                image.putpixel((i, j), pixel)
    return image

# 设置滤波器
filter = 1 / 9 * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def padding_filter(data, filter):
    """
    滤波函数，周边补零
    """
    x, y = data.shape
    filter_size, _ = filter.shape
    padding_size = int(filter_size / 2)
    data = np.pad(data, (padding_size, padding_size), 'constant')
    new = []
    for i in range(x - padding_size + 1):
        line = []
        for j in range(y - padding_size + 1):
            line.append(
                np.sum(
                    np.multiply(filter, data[i:i + filter_size,
                                             j:j + filter_size])))
        new.append(line)
    return np.array(new)


def median_filter(data, filter_size):
    """
    中值滤波
    """
    x, y = data.shape
    new = []
    for i in range(x - filter_size):
        line = []
        for j in range(y - filter_size):
            line.append(np.median(data[i:i + filter_size, j:j + filter_size]))
        new.append(line)
    return np.array(new)


if __name__ == "__main__":
    # 椒盐噪声
    pepper_noise_image = add_pepper_noise('../data/g.png')
    pepper_noise_image.show()
    pepper_noise_image.save('../result/filter/pepper.png')

    # 填充滤波
    padding_filter_image = Image.fromarray(
        padding_filter(np.array(pepper_noise_image), filter))
    padding_filter_image.show()
    padding_filter_image.save('../result/filter/padding_filter.png')

    # 高斯噪声
    gaussian_noise_image = add_gaussian_noise('../data/g.png')
    gaussian_noise_image.show()
    gaussian_noise_image.save('../result/filter/gaussian.png')

    # 中值滤波
    median_filter_image = Image.fromarray(
        median_filter(np.array(gaussian_noise_image), 3))
    median_filter_image.show()
    median_filter_image.save('../result/filter/median_filter.png')
