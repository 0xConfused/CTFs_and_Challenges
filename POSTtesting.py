#!/usr/bin/env python
__author__ = "混乱し"

import requests

def main():
    payload = 'wikipedia'
    r = requests.post('209.18.47.62', data=payload)
    print(r.text)

if __name__ == "__main__":
    main()
