import re
from hist import Histogram


content = ''

with open('equality.txt','r') as f:
    content = ''.join(line.strip() for line in f)

matches = re.findall(r'[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]',content)
print matches

