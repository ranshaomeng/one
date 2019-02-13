# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

lujing = 'e:/photo/1.jpg'
lujing1 = 'e:/photo/ddew33.jpg'
im = Image.open(lujing).convert('RGBA')
txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 200)
d = ImageDraw.Draw(txt)
# d.text((txt.size[0]-80,txt.size[1]-30),"cnBl6666666666666666666666666666666666ogs",font=fnt,fill=(255,255,255,255))
# d.text((40, 40),"cnBl6666666666666666666666666666666666ogs", fill=(0, 0, 0), font=fnt)

d.text((im.size[0] / 2, im.size[1] / 2), u'广告', fill='black', font=fnt)
out = Image.alpha_composite(im, txt)
out.save(lujing1, "png")
#Image.SAVE(new_lujing)

#out = Image.alpha_composite(base_img, txt_img)
#out.save(out_path, "png")