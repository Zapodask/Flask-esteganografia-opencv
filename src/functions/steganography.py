import cv2
import numpy as np


def get_image(image):
    return cv2.imdecode(np.fromfile(image, np.uint8), cv2.IMREAD_COLOR)


def char_generator(message):
    for c in message:
        yield ord(c)


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def encode(image, message):
    """
    Criptografar texto em imagem
    """
    img = get_image(image)
    msg = char_generator(message)
    pattern = gcd(img.shape[0], img.shape[1])

    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i + 1 * j + 1) % pattern == 0:
                try:
                    img[i - 1][j - 1][0] = next(msg)
                except StopIteration:
                    img[i - 1][j - 1][0] = 0
                    return img

    # cv2.imwrite("image.png", img)


def decode(image):
    """
    Descriptografar texto em imagem
    """
    img = get_image(image)
    pattern = gcd(len(img), len(img[0]))
    message = ""

    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i - 1 * j - 1) % pattern == 0:
                if img[i - 1][j - 1][0] != 0:
                    message = message + chr(img[i - 1][j - 1][0])
                else:
                    return message
