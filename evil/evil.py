with open('evil2.gfx','rb') as f:
    data = ''.join(i for i in f)

a = [[],[],[],[],[]]
n = 0

for i in range(len(data)-1):
    a[n].append(data[i])
    n = (n+1)%len(a)

for n,i in range(len(a)):
    with open(str(i+1),'wb') as f:
        f.write(''.join(j for j in a[i]))


