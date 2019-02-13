# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import glob

def add_num(pattern,texts):
    setFont = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', 500)
    fillColor = "#ff0000"

    for img in glob.glob(pattern):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        draw.text((image.size[0] / 2, image.size[1] / 2), texts, font=setFont, fill=fillColor)
        image.save('e:/photo/abc.jpg','jpeg')

    return 0

if __name__ == '__main__':
    pattern =  'e:/photo/1.jpg'
    add_num(pattern,u"广告在")

