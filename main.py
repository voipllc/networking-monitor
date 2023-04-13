import pcapy
from scapy.all import *

# configure PCAP
dev = "wlp3s0"
max_bytes = 1024
promiscuous = False
read_timeout = 100 # in milliseconds

# Open the network interface in promiscuous mode
pcap = pcapy.open_live(interface, 65536, 1, 0)

# Define a callback function to process packets
def handle_packet(pkt):
    pkt = Ether(pkt)
    if IP in pkt:
        print(pkt[IP].src)

# Start capturing packets
pcap.loop(-1, handle_packet)

