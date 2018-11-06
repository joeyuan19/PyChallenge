hist = {}

content = ''
with open('ocr.txt','r') as f:
    for line in f:
        line = line.strip()
        content += line
        for c in line:
            if c in hist:
                hist[c] += 1
            else:
                hist[c] = 1

rare = [i for i,j in hist.iteritems() if j < 5]

url = []
for i in rare:
    url.append((i,content.find(i)))

print sorted(url,key=(lambda n: n[1]))


