import pickle

banner = pickle.load(open('banner.p','r'))
s = ''
for i in banner:
    for j in i:
        s += j[0]*j[1]
    s += '\n'

print s

