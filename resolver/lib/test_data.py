import unittest
from StringIO import StringIO

from data import reverse_domain, DomainsFilterStream


class TestData(unittest.TestCase):
	answers = ["ru.www", "ru.yandex.www", "ru.test"]
	answers_rev = ["www.ru", "www.yandex.ru", "test.ru"]

	def test_reverse(self):
		self.assertEqual("ru.yandex.www", reverse_domain("www.yandex.ru"))
		self.assertEqual("ru.yandex.www", reverse_domain(".www.yandex.ru"))

	def test_stream(self):
		fd = StringIO("\n".join(self.answers))
		stm = DomainsFilterStream(fd, reversed=False)
		for valid, domain in zip(self.answers, stm):
			self.assertEqual(valid, domain)

	def test_stream_rev(self):
		fd = StringIO("\n".join(self.answers))
		stm = DomainsFilterStream(fd, reversed=True)
		for valid, domain in zip(self.answers_rev, stm):
			self.assertEqual(valid, domain)

if __name__ == "__main__":
	unittest.main()