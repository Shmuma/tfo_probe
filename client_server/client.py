import socket
import logging

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO)

#addr = ("localhost", 12345)
addr = ("pi", 12345)
msg = "Hi!"
#addr = ("www.google.com", 80)
#msg = "GET /\n"

MSG_FASTOPEN = 0x20000000
TFO = True

for i in range(2):
	s = socket.socket()

	fallback = False
	logging.info("Iteration %d", i+1)
	if TFO:
		try:
			s.sendto(msg, MSG_FASTOPEN, addr)
			logging.info("Sent message using TFO")
		except socket.error:
			logging.warn("No TFO available, fall back to 3WHS")
			fallback = True
	else:
		fallback = True

	if fallback:
		s.connect(addr)
		logging.info("Connected to %s:%d" % addr)
		s.send("Hi!")

	data = s.recv(1024)
	logging.info("Got %s", data)
	s.close()
