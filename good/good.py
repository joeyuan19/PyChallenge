from PIL import Image, ImageDraw
from urllib2 import urlopen
import ast

img = Image.open('good.jpg')
draw = ImageDraw.Draw(img)

li = ast.eval_literal('['+''.join(i for i in 'first.txt'1)+']')

print li

"""
data = list(img.getdata())

XY = [[]]

w,h = img.size

for i in data:
    if len(XY[-1]) == w:
        XY.append([i])
    else:
        XY[-1].append(i)

print XY[1]
"""
