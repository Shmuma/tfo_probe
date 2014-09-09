"""
It's simple conniction establishment using scapy.
"""

import random
import scapy.all as scapy

def rand_short():
	return random.randint(1024, 65536)


src_host = "192.168.100.12"
dst_host = "192.168.100.4"
src_port = rand_short()
dst_port = 12345
my_seq = rand_short()
it_seq = 0

# establish connection
#eth = scapy.Ether(src="00:00:00:00:00:00", dst="00:00:00:00:00:00", type=0)

ip = scapy.IP(src=src_host, dst=dst_host)

p_syn = ip/scapy.TCP(sport=src_port, dport=dst_port, flags='S', seq=my_seq)
print p_syn.summary()
r = scapy.sr1(p_syn)
print r.summary()

it_seq = r.seq+1
my_seq += 1

p_ack = ip/scapy.TCP(sport=src_port, dport=dst_port, flags='A', seq=my_seq, ack=it_seq)
print p_ack.summary()
scapy.send(p_ack)

# have connection, send some data
p_dat = ip/scapy.TCP(sport=src_port, dport=dst_port, seq=my_seq, flags='PA', ack=it_seq)/"scapy!"
print p_dat.summary()
r = scapy.sr1(p_dat)
print r.summary()

r.show()

it_seq += len(r.load)
my_seq += len(p_dat.load)

p_ack = ip/scapy.TCP(sport=src_port, dport=dst_port, seq=my_seq, flags='A', ack=it_seq)
print p_ack.summary()
scapy.send(p_ack)

#seq_no += 1

# close connection
p_ack = ip/scapy.TCP(sport=src_port, dport=dst_port, seq=my_seq, flags='FA', ack=it_seq)
r = scapy.sr1(p_ack)
print r.summary()

my_seq += 1
it_seq += 1

p_ack = ip/scapy.TCP(sport=src_port, dport=dst_port, seq=my_seq, flags='A', ack=it_seq)
scapy.send(p_ack)

# connection closed