import sys
import logging
import socket

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO)

addr = ("localhost", 12345)

TCP_FASTOPEN = 23

s = socket.socket()
s.bind(addr)
s.setsockopt(socket.SOL_TCP, TCP_FASTOPEN, 100)
s.listen(1)

while True:
	logging.info("Socket ready, wait for connection on %s:%d" % addr)
	conn, caddr = s.accept()
	logging.info("Client from %s:%d" % caddr)

	while True:
		data = conn.recv(1024)
		if not data:
			break
		logging.info("Got %s", data)
		conn.send("Hello!")

	conn.close()

