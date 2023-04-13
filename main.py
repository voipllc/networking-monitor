import pcapy
from scapy.all import *

# configure PCAP
dev = "wlp3s0"
max_bytes = 1024
promiscuous = False
read_timeout = 100 # in milliseconds

# open PCAP interface
pcap = pcapy.open_live(dev, max_bytes, promiscuous, read_timeout)

# process packets
while True:
    try:
        # read packet
        _, packet_data = pcap.next()

        # parse packet using Scapy
        packet = Ether(packet_data)

        # print source and destination IPv4 addresses
        if IP in packet:
            ip_layer = packet[IP]
            print(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")
    except pcapy.PcapError:
        continue

