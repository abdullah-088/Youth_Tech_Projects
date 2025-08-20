🐍 Packet Sniffer

A simple Python packet sniffer built with Scapy to capture and analyse network traffic. Ideal for learning how data travels across networks and understanding common protocols like TCP, UDP, and ICMP.

🚀 Features

- Captures live IP packets from your network.
- Displays source and destination IP addresses.
- Identifies the protocol (TCP, UDP, ICMP).
- Shows the first 100 bytes of payload (if present).
- Limits capture to a specific number of packets (default: 30).

🛠️ Requirements

Python 3.7+
[Scapy](https://scapy.net/)
Install Scapy using pip:
bash
pip install Scapy
⚠️ Sniffing packets may require administrative/root privileges.

 📌 Usage
Run the script:bash
python sniffer.py
Example:
Starting packet capture...

[+] Src: 192.168.1.5 --> Dst: 8.8.8.8 | Protocol: TCP
    Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n...'
------------------------------------------------------------
📁 Packet-Sniffer
 ┣ 📄 sniffer.py
 ┗ 📄 README.md
⚡ Example Output
Starting packet capture...

[+] Src: 10.0.0.2 --> Dst: 172.217.16.196 | Protocol: UDP
    Payload: b'\x12\x34\x56\x78...'
------------------------------------------------------------
[+] Src: 192.168.1.5 --> Dst: 8.8.8.8 | Protocol: TCP
    Payload: b'GET / HTTP/1.1\r\nHost: example.com\r\n...'
------------------------------------------------------------
🔗 Resources
[Scapy Documentation] (https://scapy.readthedocs.io/)
[TCP/UDP/ICMP Overview] (https://www.cloudflare.com/learning/network-layer/what-is-tcp/)


