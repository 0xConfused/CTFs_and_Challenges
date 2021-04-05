#!/usr/bin/env python3

import requests
import hashlib

req = requests.session()
URL = 'http://139.59.178.146:31249'

def getPlaintext():
    html = req.get(URL)
    plaintext = html.text.split("<h3 align='center'>")[1].split("</h3>")[0]
    print("plaintext is: "+plaintext)
    return plaintext

def getHash(plaintext):
    payload = hashlib.md5(plaintext.encode())
    print("md5 hash is: "+payload.hexdigest())
    return payload.hexdigest()

def sendPOST(postData):
    rtnHtml = req.post(url=URL, data=postData)
    print(rtnHtml.text)

def createPOST(hashVal):
    data = dict(hash=hashVal)
    print(data)
    return data

def main():
    plaintext = getPlaintext()
    md5hash = getHash(plaintext)
    post = createPOST(md5hash)
    sendPOST(post)
    

if __name__ == '__main__':
    main()
