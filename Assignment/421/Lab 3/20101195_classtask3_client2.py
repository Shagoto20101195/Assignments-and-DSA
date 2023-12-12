# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:02:05 2023

@author: User
"""

import socket
HEADER = 64
FORMAT = 'utf-8'

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050 # Do not use well known. Can cause error

disconnect_msg = "End"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT) # in bytes
    send_length += b" "*(HEADER - len(send_length))
    
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT)) # 2048. Server can send big message

msg = f"The hostname of the client is {socket.gethostname()} and IP Server: {SERVER}"

while True:
  msg = input("Enter text: ")

  if msg == disconnect_msg:
    send(msg)
    break
  else:
    send(msg)
