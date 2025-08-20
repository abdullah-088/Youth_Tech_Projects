from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# This function will be called for every packet captured
def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        # Match protocol number to name
        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        elif proto == 1:
            protocol = "ICMP"
        else:
            protocol = str(proto)

        print(f"[+] Src: {src_ip} --> Dst: {dst_ip} | Protocol: {protocol}")

        # Show first 100 bytes of payload (if present)
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload: {payload[:100]}")
        print("-" * 60)

# Start sniffing packets
print("Starting packet capture...\n")
sniff(filter="ip", prn=process_packet, store=False, count=30)
