import psutil
import socket
from scapy.all import DNS, DNSQR
from scapy.all import sniff
from variables import *
from features.fw_operations import *

def get_network_adapters():
        adapters = []
        for iface, nic_data in psutil.net_if_addrs().items():
            for addr in nic_data:
                if addr.family == socket.AF_INET:
                    adapters.append(iface)
                    break
        return adapters

def get_current_adapter():
        active_ip = socket.gethostbyname(socket.gethostname())
        adapters = get_network_adapters()
        for adapter in adapters:
            iface = psutil.net_if_addrs()[adapter]
            for nic in iface:
                if nic.family == socket.AF_INET and nic.address == active_ip:
                    return adapter
        
        return None

def start_sniffing(packet):
    checked_domains= set()
    print("....")
    if DNS in packet and packet[DNS].qr == 0:
        target_domain = packet[DNSQR].qname.decode('utf-8')
        for item in filtered_data['items']:
            if item['url'] in target_domain and item['url'] not in checked_domains:
                print(f"Potential malicious domain is detected: {target_domain} and blocked.")
                user_input = input("Do you want to remove block? (yes/no)")
                if user_input == "yes":
                    for item in filtered_data['items']:
                        if item['url'] == target_domain:
                            unblock_ips_temporarily(item['ip'])
                checked_domains.add(item['url'])