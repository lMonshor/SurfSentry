import psutil
import socket
from scapy.all import *
import db.db_operations
from mitmproxy import http


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

blocked_data = db.db_operations.custom_query('select url from blocked_data where current_status = "blocked"')
mylist = ['facebook.com']
def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url in mylist:
        print("aaaaa")
