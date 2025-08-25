from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        elif proto == 1:
            protocol = "ICMP"
        else:
            protocol = str(proto)

        print(f"[+] Src: {src_ip} --> Dst: {dst_ip} | Protocol: {protocol}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload: {payload[:100]}")
        print("-" * 60)

print("Starting packet capture...\n")
sniff(filter="ip", prn=process_packet, store=False, count=30)
