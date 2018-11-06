from PIL import Image

def to_XY(data,w):
    XY = [[]]
    for i in range(len(data)):
        XY[-1].append(data[i])
        if len(XY[-1]) == w:
            XY.append([])
    return XY[:-1]

def rotate(li):
    _li = li[::-1]
    idx = _li.index(max(_li))
    _li = _li[idx:]+_li[:idx]
    return _li[::-1]

a =   [1,1,1,1,1,1,1,5,2,2,2,2,2,2]
print rotate(a)

img = Image.open('mozart.gif')
pix = list(img.getdata())
w,h = img.size

XY = to_XY(pix,w)
new = []
for i in XY:
    new.append(rotate(i))

new_img = []
for i in new:
    new_img += i

nimg = Image.new('P',(w,h))
nimg.putdata(new_img)
nimg.show()
