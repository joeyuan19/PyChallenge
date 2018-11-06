

"""
next_id = '90052'
while True:
    with open('channel/'+next_id+'.txt') as f:
        content = ''.join(i.strip() for i in f)
    print content
    next_id = content[content.rfind(' ')+1:]
   """

from zipfile import ZipFile

z = ZipFile(open('channel.zip','r'))
print z
print z.comment

