import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# msg = s.recv(1024)
# print(msg.decode())


full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)


# s.settimeout(2.0)
# full_msg = ''
# while True:
#     try:
#         msg = s.recv(8)
#     except Exception as e:
#         msg = ''
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
# print(full_msg)


# import select
# s.setblocking(0)
# ready = select.select([s], [], [], 2)

# full_msg = ''
# if ready[0]:
#     while True:
#         try:
#             msg = s.recv(8)
#         except Exception as e:
#             print(e)
#             s.close()
#             msg = ''
#         if len(msg) <= 0:
#             break
#         full_msg += msg.decode("utf-8")
# print(full_msg)