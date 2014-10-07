import logging

import thread
import socket
from threading import Thread

class ResolverWorker(Thread):
	"""
	Threaded resolver for hostnames
	"""
	def __init__(self, queue, **kargs):
		super(ResolverWorker, self).__init__(**kargs)
		self.queue = queue


	def run(self):
		ident = thread.get_ident()
		logging.info("Worker %x started" % ident)
		while True:
			domain = self.queue.get()
			if domain is None:
				logging.info("Worker %x terminating", ident)
				break
			logging.info("%x: got %s", ident, domain)
			try:
				info = socket.getaddrinfo(domain, 0, socket.AF_INET, socket.SOCK_STREAM)
				for _, _, _, _, sockaddr in info:
					logging.info("%x: %s -> %s", ident, domain, sockaddr[0])				
			except socket.gaierror:
				logging.info("%x: Not found", ident)		