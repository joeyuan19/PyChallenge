from PIL import Image,ImageDraw
import ast

with open('good/first.txt','r') as f:
    first = ''.join(i for i in f)

with open('good/second.txt','r') as f:
    second = ''.join(i for i in f)

first = ast.literal_eval(first)
second = ast.literal_eval(second)

img = Image.open('good/good.jpg')
pix = img.getdata()

w,l = img.size

XY = [[]]
for i in pix:
    if len(XY[-1]) == l:
        XY.append([])
    else:
        XY[-1].append(i)

draw = ImageDraw.Draw(img)

L = len(first)
s = []
i = 0
while i < L-1:
    s.append((first[i],first[i+1]))
    i += 2
first = s

for j in range(len(first)-1):
    draw.line((first[j][0],first[j][1],first[j+1][0],first[j+1][1]),fill=(0,255,0),width=2)


L = len(second)
s = []
i = 0
while i < L-1:
    s.append((second[i],second[i+1]))
    i += 2
second = s


for j in range(len(second)-1):
    draw.line((first[j][0],first[j][1],first[j+1][0],first[j+1][1]),fill=(255,0,0),width=2)

img.save('good/test.png')



