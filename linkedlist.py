from urllib2 import urlopen

ids = []

next_id = str(int('16044')/2)
while True:
    ids.append(next_id)
    link = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+next_id)
    text = ''.join(i.strip() for i in link)
    next_id = text[text.rfind(' ')+1:]
    print next_id






