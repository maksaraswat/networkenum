#!/usr/bin/python

import string, optparse, sys, icmp_ping, arp_ping
from scapy.all import *

def main():
	try:
		parser = optparse.OptionParser('usage: ' + sys.argv[0] + ' -H <target ip>')
		parser = optparse.OptionParser()
		parser.add_option('-H', dest='host', help='specify IP address or subnet like 192.168.1.1-100 for ICMP Ping')
		parser.add_option('-A', dest='host', help='specify IP address or subnet like 192.168.1.1-100 for Arping')		
		(options, args) = parser.parse_args()
		host=options.host
		if options.host !=None:
			if sys.argv[1] == "-H":
				icmp_ping.icmpping(host)
			if sys.argv[1] == "-A":		
				arp_ping.arpping(host)			
		else:
			print parser.usage
		
	except Exception, e:
		print e

if __name__ == '__main__':
	main()
