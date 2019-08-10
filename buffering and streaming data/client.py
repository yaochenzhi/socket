import socket
import select
import errno


HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = "1234"

my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}"
client_socket.send(username_header + username)

while True:
	msg = input(f"{my_username} > ")

	if msg:
		msg = msg.encode('utf-8')
		msg_header = f"{len(msg) :<{HEADER_LENGTH}}".encode('utf-8')
		client_socket.send(msg_header + msg)

	try:
		while True:
			username_header = client_socket.recv(HEADER_LENGTH)
			if not len(username_header):
				sys.exit("Connection closed by server!")
			username_len = int(username_header.decode('utf-8').strip())
			username = client_socket.recv(username_len).decode('utf-8')

			
	except Exception as e:
		print(e)

