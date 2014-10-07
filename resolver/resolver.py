import sys
import logging
import argparse
import socket
import Queue as queue

from lib.data import DomainsFilterStream
from lib.workers import ResolverWorker

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

	parser = argparse.ArgumentParser(description="Perform parallel resolution of domain names to IP addresses")
	parser.add_argument("domains", type=str, nargs=1, help="File name with domains to be processed")
	parser.add_argument("--reversed", action="store_true",
		help="Process domains in reversed-dot notation. I.e: ru.yandex.www")
	parser.add_argument("--threads", action="store", type=int, help="Count of threads to run", default=8)
	parser.add_argument("--no-stats", action="store_true", default=False, help="Suppres stats after run")

	args = parser.parse_args()
	print args

	queue = queue.Queue()
	
	# launch workers
	workers = [ResolverWorker(queue) for _ in range(args.threads)]
	map(lambda w: w.start(), workers)

	# process domains file
	with open(args.domains[0], 'r') as fd:
		domains_stream = DomainsFilterStream(fd, reversed=args.reversed)
		for domain_txt in domains_stream:
			queue.put(domain_txt)

	# put N None objects which signals workers to exit
	for _ in range(args.threads):
		queue.put(None)

	map(lambda w: w.join(), workers)