#!/usr/bin/python

#!/usr/bin/python

import string, optparse, sys, icmp_ping, arp_ping, syn_scan
from scapy.all import *
			
# This is the main program that call other modules icmp_ping, arp_ping and syn_scan
def main():
	try:
				
		parser = optparse.OptionParser('usage: ' + sys.argv[0] + ' <-h for help>')
		parser.add_option('-I', dest='host', help='specify IP address or subnet like 192.168.1.1-100 for ICMP Ping')
		parser.add_option('-A', dest='host', help='specify IP address or subnet like 192.168.1.1-100 for Arping')
		parser.add_option('-S', dest='host', help='specify IP address and port (eg. 80 or 435-445) for SYN Scan')		
		(options, args) = parser.parse_args()
		host=options.host
		if options.host !=None:
			if sys.argv[1] == "-I":
				icmp_ping.icmpping(host)
			if sys.argv[1] == "-A":		
				arp_ping.arpping(host)	
			if sys.argv[1] == "-S":
				if len(sys.argv) == 4:
					if "-" in sys.argv[3]:			
						alpha = []
						for z in sys.argv[3].split("-"):
							alpha.append(z)
						syn_scan.synscan(sys.argv[2],int(alpha[0]),int(alpha[1]))
					else:				
						beta = []						
						for x in sys.argv[3].split(","):	
							beta.append(int(x))				
						syn_scan.synscan2(sys.argv[2], beta)
				else:
					print "[-] Missing arguments...Provide IP and Port(s) both"
		else:
			print parser.usage
		
	except Exception, e:
		print e

if __name__ == '__main__':
	main()
