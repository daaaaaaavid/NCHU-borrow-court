import numpy as np
import pytesseract
import PIL.Image
import PIL.ImageDraw
from PIL import *
from PIL import ImageEnhance
from PIL import Image
import cv2
import matplotlib.pyplot as plt
# Important variables

show_image = False


# ------- DO NOT EDIT BELOW -------

# Code from https://stackoverflow.max-everyday.com/2019/06/python-opencv-denoising/
def getPixel(image, x, y, G, N):
    L = image.getpixel((x, y))
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0
    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None


def clearNoise(image, G, N, Z):
    draw = PIL.ImageDraw.Draw(image)

    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = getPixel(image, x, y, G, N)
                if color != None:
                    draw.point((x, y), color)

    return image


class CaptchaBroker():

    def decode(self, image_path, user_tesseract_cmd):
        # open image
        image = Image.open(image_path)
        # image.show()
        # enhancer = ImageEnhance.Contrast(image)
        # image = enhancer.enhance(3.0)
        # image.show()

        arr = np.array(image)
        arr = cv2.fastNlMeansDenoisingColored(arr, None, 10, 10, 7, 21)
        arr = Image.fromarray(arr)
        # arr.show()

        # Very important, tesseract-ocr path here
        pytesseract.pytesseract.tesseract_cmd = user_tesseract_cmd
        code = pytesseract.image_to_string(arr)

        return code

if __name__ == '__main__':
    pass
