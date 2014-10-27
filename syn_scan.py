#!/usr/bin/python

import string, sys,optparse
from scapy.all import *

# Removes "Begin emission:..............................Finished to send 1 packets" message.
conf.verb=0

# Removes "WARNING: Mac address to reach destination not found. Using broadcast" message.    
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# This function is called when range of port is provided e.g. 80-100 
def synscan(host,port,port2):
	try:
		ans, uans = sr(IP(dst=host)/TCP(sport=RandShort(),dport=(port,port2),flags="S"),timeout=0.5)
		if ans:
			ans.summary( lambda(s,r): r.sprintf("%IP.src% \t %TCP.sport% \t %TCP.flags%") )
		else:	
			print "[-] Cannot get to {0}...".format(host)
	except Exception, e:
		print e

# This function is called when only specific ports are scanned 
# and not a range e.g. 80,100 
def synscan2(host,port):
	try:
		ans, uans = sr(IP(dst=host)/TCP(sport=RandShort(),dport=port,flags="S"),timeout=0.5)
		if ans:
			ans.summary( lambda(s,r): r.sprintf("%IP.src% \t %TCP.sport% \t %TCP.flags%") )
		else:
			print "[-] Cannot get to {0}...".format(host)	
	except Exception, e:
		print e

def main():
	try:
		parser = optparse.OptionParser('usage: ' + sys.argv[0] + ' -S <target ip> <port(s)>')
		parser.add_option('-S', dest='host', help='specify IP address and a port for for SYN Scan')		
		(options, args) = parser.parse_args()
		host=options.host
		if options.host !=None:
			if sys.argv[1] == "-S":
				if "-" in sys.argv[3]:			
					alpha = []
					for z in sys.argv[3].split("-"):
						alpha.append(z)
					synscan(sys.argv[2],int(alpha[0]),int(alpha[1]))
				else:				
					beta = []						
					for x in sys.argv[3].split(","):	
						beta.append(int(x))				
					synscan2(sys.argv[2], beta)
		else:
			print parser.usage
		
	except Exception, e:
		print e

if __name__ == '__main__':
	main()
