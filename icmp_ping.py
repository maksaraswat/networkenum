#!/usr/bin/python

import string, sys
from scapy.all import *

# This function uses scapy for ICMP Ping iterating over tuples of answered packed.
def icmpping(host):
	try:
		ans,unans=sr(IP(dst=host)/ICMP(), inter=0.05,timeout=0.5)
#		ans.summary(lambda (s,r): r.sprintf(" [*] %IP.src% is alive and is Linux" if r.ttl < 65 else " [*] %IP.src% is alive and is Windows"))
		for s,r in ans:
			
			if r.ttl < 65:
				print "{0} is alive and is Linux(TTL = {1})".format(str(r.src), str(r.ttl))
			else:
				print "{0} is alive and is Windows(TTL = {1})".format(str(r.src), str(r.ttl))	
	except Exception, e:
		print e

def main():
	icmpping(host)

if __name__ == '__main__':
	main()
