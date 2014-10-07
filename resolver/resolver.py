import sys
import logging
import argparse
import socket
import Queue as queue

from lib import data

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

	parser = argparse.ArgumentParser(description="Perform parallel resolution of domain names to IP addresses")
	parser.add_argument("domains_files", type=str, nargs="+", help="File name with domains to be processed")
	parser.add_argument("--reversed", action="store_true", help="Process domains in reversed-dot notation. I.e: ru.yandex.www")

	args = parser.parse_args()
	print args