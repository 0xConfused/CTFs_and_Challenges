#!/usr/bin/env python3

import requests
import hashlib
import re

req = requests.session()
url = "http://139.59.178.146:31249"

### GET Request
rget = req.get(url)
html = str(rget.content)     # Saving the GET request

### Strip HTML and Split Random String
print(html)
plaintext = html.split("<h3 align='center'>")[1].split("</h3>")[0]

### MD5 Encrypt
mdhash = hashlib.md5(plaintext).hexdigest()

### POST Request
data = dict(hash=mdhash)
rpost = req.post(url=url, data=data)

print(rpost.text)