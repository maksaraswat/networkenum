#!/usr/bin/python

import string, sys
from scapy.all import *

# This function uses scapy for ARP Ping iterating over tuples of answered packed.
def arpping(host):
	try:
		ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=host),timeout=2)
#		ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )		
		for s,r in ans:
			print "{0} is the MAC address for host {1}".format(r.src, r.psrc)
	except Exception, e:
		print e

def main():
	arpping(host)

if __name__ == '__main__':
	main()
