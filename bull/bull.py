def to_3(n):
    s = ''
    while n > 0:
        r = n%3
        s = str(r) + s
        n = n/3
    return int(s)

def f(n):
    s = str(n)
    buf = s[0]
    i = 1
    out = []
    while i < len(s):
        if buf[-1] != s[i]:
            out.append((len(buf),buf[-1]))
            buf = s[i]
        else:
            buf += s[i]
        i += 1
    if len(buf) > 0:
        out.append((len(buf),buf[-1]))
    return ''.join(str(i)+str(j) for i,j in out) 

a = [1, 11, 21, 1211, 111221]


for i in range(26):
    a.append(f(a[-1]))
for i in a:
    print i
print len(a[30])



