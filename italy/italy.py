from PIL import Image

img = Image.open('wire.png')
pix = list(img.getdata())
new = Image.new('RGB',(100,100))
im = new.load()

def spiril_gen(M,N):
    i,j = 0,0
    max_i = M
    min_i = -1
    max_j = N
    min_j = 0
    di = 0
    dj = 0

    for n in range(N*M):
        yield i,j
        if i == max_i and j == max_j:
            di = -1
            dj = 0
            min_i += 1
        elif i == max_i and j == max(min_j,0):
            di = 0
            dj = 1
            max_j -= 1
        elif i == max(min_i,0) and j == max_j:
            di = 0
            dj = -1
            min_j += 1
        elif i == max(min_i,0) and j == max(min_j,0):
            di = 1
            dj = 0
            max_i -= 1
        i,j = i+di,j+dj

#   (min_i,min_j) ................... (max_i,min_j)
#          (+1,0) .                 . (0,+1)
#                 .                 .
#                 .                 .
#                 .                 .
#          (0,-1) .                 . (-1,0)
#   (min_i,max_j) ................... (max_i,max_j)

n = 0
for x,y in spiril_gen(100,100):
    im[x,y] = pix[n]
    n += 1

new.show()


