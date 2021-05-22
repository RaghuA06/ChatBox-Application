#Raghu Alluri
#May 2021

import socket
import sys
import time

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8000

new_socket.bind((host_name, port))
print("The server has binded the host and port sucessfully!")
print("Your IP is:{}\n".format(s_ip))

name = input("Enter name:")
new_socket.listen(1)

conn, addr = new_socket.accept()
print("\nReceived connection from {}".format(addr[0]))
print("Connection is established. Connected from:{}".format(addr[0]))

client = (conn.recv(1024)).decode()
print("\n{} has connected.".format(client))
conn.send(name.encode())

while True:
    message = str(input('\nMe:'))
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("\n{}:{}".format(client, message))

