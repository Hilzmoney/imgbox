#!/usr/bin/env python

from imgbox import imgbox
from PIL import Image
from os.path import abspath, dirname, join

DIR = dirname(abspath(__file__))
img = join(DIR, 'test.webp')
img = Image.open(img)
imgbox(
    img,
    (
        (
            '测试1',
            (30, 30, 100, 300)  # x y  x_end y_end
        ),
        ('测试2', (60, 60, 200, 200)),
        ('测试3', (100, 200, 100, 300)),
        ('测试4', (300, 300, 20, 100))))
img.save(join(DIR, 'out.webp'), quality=80)
