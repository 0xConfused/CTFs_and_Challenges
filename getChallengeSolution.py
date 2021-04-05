#!/usr/bin/env python3

import requests
import hashlib
import re

req = requests.session()
url = "http://139.59.178.146:31249"

### GET Request
rget = req.get(url)
html = rget.content     # Saving the GET request

### Strip HTML
def html_tags(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

### Split Random String
out1 = html_tags(html)
out2 = out1.split('string')[1]
out3 = out2.rstrip()

### MD5 Encrypt
mdHash = hashlib.md5(out3).hexdigest()

### POST Request
data = dict(hash=mdhash)
rpost = req.post(url=url, data=data)

print(rpost.text)