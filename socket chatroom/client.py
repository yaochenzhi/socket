import socket
import select
import errno
import sys


HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

my_username = input("Username: ")
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


while True:

	msg = input(f"{my_username} > ")
	# msg = ""  # get rid of input blocking and recv msg from other user in the chatroom immediately
	if msg:
		msg = msg.encode('utf-8')
		msg_header = f"{len(msg):<{HEADER_LENGTH}}".encode('utf-8')
		client_socket.send(msg_header + msg)

	try:
		while True:
			username_header = client_socket.recv(HEADER_LENGTH)
			if not username_header:
				sys.exit("Connection closed by the server")
			username_len = int(username_header.decode('utf-8').strip())
			username = client_socket.recv(username_len).decode('utf-8')

			msg_header = client_socket.recv(HEADER_LENGTH)
			# if not msg_header:
			# 	sys.exit("Connection closed by the server")
			msg_len = int(msg_header.decode('utf-8').strip())
			msg = client_socket.recv(msg_len).decode('utf-8')
			
			print(f"{username}: {msg}")
	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			sys.exit(f"Reading error: {str(e)}")
		continue
	except Exception as e:
		sys.exit(f"General error: {str(e)}")