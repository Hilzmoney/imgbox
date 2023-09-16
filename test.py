#!/usr/bin/env python

from imgbox import imgbox
from PIL import Image
from os.path import abspath, dirname, join

DIR = dirname(abspath(__file__))
img = join(DIR, 'test.webp')
img = Image.open(img)
imgbox(img, ('测试', (30, 30, 60, 60)))
img.save(join(DIR, 'box.webp'), quality=80)
