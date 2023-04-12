import psutil
import uuid
import socket

def get_ip_and_mac_addresses():
    ip_addresses = []
    mac_addresses = []

    # Get all the network interfaces
    interfaces = psutil.net_if_addrs()

    for interface_name, interface_addresses in interfaces.items():
        # Get the IP address(es) for this interface
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                ip_addresses.append(address.address)

        # Get the MAC address for this interface
        if interface_name == 'lo':
            continue
        mac_addresses.append(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                                      for ele in range(0,8*6,8)][::-1]))

    return ip_addresses, mac_addresses

ip_addresses, mac_addresses = get_ip_and_mac_addresses()
print(f"IP addresses: '{', '.join(ip_addresses)}'")
print(f"MAC addresses: '{', '.join(mac_addresses)}'")
