def reverse_domain(domain_str):
	"""
	Perform reverse of dot-separated domain. Return reversed version
	"""
	v = domain_str.split(".")
	v.reverse()
	return ".".join(filter(len, v))


class DomainsFilterStream(object):
	"""
	Process domain stream by filtering empty lines and perform optional reversion
	"""
	def __init__(self, stream, reversed=False):
		self.reversed = reversed
		self.stream = stream

	def __iter__(self):
		return self

	def next(self):
		"""
		Read next non-empty line from underlying stream and
		reverse domain if needed
		"""
		while True:
			line = self.stream.readline()
			if len(line) == 0:
				raise StopIteration
			line = line.strip()
			if len(line) == 0:
				continue
			if self.reversed:
				return reverse_domain(line)
			return line