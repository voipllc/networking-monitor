import pcapy
from scapy.all import *

# Define the network interface to capture on
interface = 'wlp3s0'

# Open the network interface in promiscuous mode
pcap = pcapy.open_live(interface, 65536, 1, 0)

# Define a callback function to process packets
def handle_packet(pkt):
    pkt = Ether(pkt)
    if IP in pkt:
        print(pkt[IP].src)

# Start capturing packets
pcap.loop(-1, handle_packet)

