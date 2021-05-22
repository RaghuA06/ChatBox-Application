#Raghu Alluri
#May 2021

import socket
import sys
import time

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8000

print("This is your IP address:{}".format(ip))
server_host = input("Enter server's IP address:")
name =  input("Enter your name:")

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print('\n{} has joined...'.format(server_name))
while True:
    message = (socket_server.recv(1024)).decode()
    print("\n{}:{}".format(server_name, message))
    message = str(input("\nMe:"))
    socket_server.send(message.encode())


