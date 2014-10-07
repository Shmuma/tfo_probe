import sys
import logging
import argparse
import socket
import Queue as queue

from lib import data

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
	
	with open(args.domains[0], 'r') as fd:
		domains_stream = data.DomainsFilterStream(fd, reversed=args.reversed)
		for domain_txt in domains_stream:
			print domain_txt