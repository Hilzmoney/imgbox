#!/usr/bin/env python

from os.path import abspath, dirname, join
from PIL import ImageDraw, ImageFont

DIR = dirname(dirname(abspath(__file__)))

font_path = join(DIR, 'font/DroidSansFallback.ttf')
font = ImageFont.truetype(font_path, 20, encoding="utf-8")


def imgbox(img, name_box_li):
  canvas = ImageDraw.Draw(img)

  n = 0
  for (name, box) in name_box_li:
    p1 = box[:2]
    p2 = box[2:]
    n += 1
    color = [255, 255, 255]
    color[n % 3] = 0
    color = tuple(color)
    canvas.text([p1[0] + 5, p1[1] + 10],
                name,
                color,
                font=font,
                stroke_width=1,
                stroke_fill=(0, 0, 0))
    canvas.rectangle(xy=(p1[0], p1[1], p1[0] + p2[0], p1[1] + p2[1]),
                     fill=None,
                     outline=color,
                     width=2)
  return
