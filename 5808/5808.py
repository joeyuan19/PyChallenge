from PIL import Image

img1 = Image.open('cave.jpg')
w,h = img1.size
img2 = Image.new("RGB",(w,h),"white")
img3 = Image.new("RGB",(w,h),"white")

pix1 = img1.getdata()
pix2 = []
pix3 = []

even = True
for i in pix1:
    if even:
        pix2.append(i)
    else:
        pix3.append(i)
    even = not even

print w*h
w,h = img2.size
print w*h
print len(pix1)
print len(pix2)
print len(pix3)

img2.putdata(pix2)
img3.putdata(pix3)

img2.save("img2.jpg")
img3.save("img3.jpg")

