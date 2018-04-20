import logging
import socket

from responses import http_response
from routing import route_request

# https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

# https://docs.python.org/3.3/library/socket.html
#
# Running an example several times with too small delay between executions, could lead to this error:
#
# OSError: [Errno 98] Address already in use
# This is because the previous execution has left the socket in a TIME_WAIT state, and can’t be immediately reused.
#
# There is a socket flag to set, in order to prevent this, socket.SO_REUSEADDR:
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((HOST, PORT))
# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.


server_socket = socket.socket()
server_socket.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1)

hostname = 'localhost'
port = 23456

server_socket.bind((hostname, port))
server_socket.listen(1000)

logging.debug("Starting server...")

while True:
    c, address = server_socket.accept()
    request = c.recv(4096).decode('utf-8')
    lines = request.split('\r\n')
    first_line = lines[0]

    logging.debug(first_line)

    method, path, version = first_line.split()
    response = route_request(path)
    prepared_response = http_response(response)
    c.sendall(prepared_response)
    c.close()
