#!/usr/bin/env python3

##  - CLIENT.PY -  ##

import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER =  "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def start():
    
    print("['q' to quit] Input to send: ", end='\n')
    while True:
        print(">", end = " ")
        msg_text = input()
        if msg_text == 'q':
            break
        send(msg_text)
        
    send(DISCONNECT_MESSAGE)

print("[STARTING] client is starting...", end='\n')
start()