#!/usr/bin/env python3

##  - SERVER.PY -  ##

import socket
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# handles existing connections
# runs for each connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.", end='\n')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[CONNECTION ENDED] connection with {addr} ended", end='\n')
            else:
                print(f"[{addr}]  --  {msg}", end='\n')

    conn.close()

# handles new connections
def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}", end='\n')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        time.sleep(0.1)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}", end='\n')
        

print("[STARTING] server is starting...", end='\n')
start()
