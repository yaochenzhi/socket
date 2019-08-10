import socket
import time
from datetime import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

HEADERSIZE = 10
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    # clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    # clientsocket.close()
    msg = "Welcome to the server!"
    msglen = len(msg)
    msg = f"{msglen:<{HEADERSIZE}}" + msg
    clientsocket.send(bytes(msg, "utf-8"))

    # keep the socket and send another new msg to be received and buffered from the client
    while True:
        time.sleep(3)
        print(f"The time is {datetime.now().timestamp()}!")

        msg = f"Welcome to the server! Current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!"
        msglen = len(msg)
        msg = f"{msglen:<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))

