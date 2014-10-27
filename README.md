networkenum
===========

Using Scapy framework for enumerating a network. networkenum.py is the main script that calls other scripts "icmp_ping.py", "arp_ping.py" and syn_scan.py. As more features will be added, networkenum.py will be updated to call them. You can read more about the project at my blog http://blog.l3g3ndary.org.

Shout Outs:

Special thanks to Dan Melfi for helping me whenever I got stuck.

+++ networkenum.py +++

root@kali:~# sudo python networkenum.py --help
WARNING: No route found for IPv6 destination :: (no default route?)
Usage: networkenum.py <-h for help>

Options:
  -h, --help  show this help message and exit
  -I HOST     specify IP address or subnet like 192.168.1.1-100 for ICMP Ping
  -A HOST     specify IP address or subnet like 192.168.1.1-100 for Arping
  -S HOST     specify IP address and port (eg. 80 or 435-445) for SYN Scan

+++ ICMP Ping +++

root@kali:~# sudo python networkenum.py -I  192.168.1.23-27
WARNING: No route found for IPv6 destination :: (no default route?)
[*] 192.168.1.23 is alive and is Windows(TTL = 128)
[*] 192.168.1.24 is alive and is Windows(TTL = 128)
[*] 192.168.1.25 is alive and is Windows(TTL = 128)

+++ ARP Ping +++

root@kali:~# sudo python networkenum.py -A  192.168.1.23-27
WARNING: No route found for IPv6 destination :: (no default route?)
[*] 0c:00:29:58:12:3c is the MAC address for host 192.168.1.23
[*] b9:0d:6f:2e:ae:26 is the MAC address for host 192.168.1.24
[*] 01:ce:30:30:13:3c is the MAC address for host 192.168.1.25

+++ SYN Scan +++

root@kali:~# sudo python networkenum.py -S  192.168.1.23 445-450
WARNING: No route found for IPv6 destination :: (no default route?)
192.168.1.23 	 microsoft_ds 	 SA
192.168.1.23 	 446 	 RA
192.168.1.23 	 447 	 RA
192.168.1.23 	 448 	 RA
192.168.1.23 	 449 	 RA
192.168.1.23 	 450 	 RA

root@kali:~# sudo python networkenum.py -S  192.168.1.23 445,3389
WARNING: No route found for IPv6 destination :: (no default route?)
192.168.1.23 	 microsoft_ds 	 SA
192.168.1.23 	 3389 	 SA
