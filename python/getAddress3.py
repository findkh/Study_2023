import netifaces

def get_ip_and_mac_addresses():
    ip_addresses = []
    mac_addresses = []

    # Get all the network interfaces
    interfaces = netifaces.interfaces()

    for interface_name in interfaces:
        # Get the IP address(es) for this interface
        addresses = netifaces.ifaddresses(interface_name)
        if netifaces.AF_INET in addresses:
            ip_addresses.append(addresses[netifaces.AF_INET][0]['addr'])

        # Get the MAC address for this interface
        if netifaces.AF_LINK in addresses:
            mac_addresses.append(addresses[netifaces.AF_LINK][0]['addr'])

    return ip_addresses, mac_addresses

ip_addresses, mac_addresses = get_ip_and_mac_addresses()
ip_addresses_string = "', '".join(filter(None, ip_addresses))
mac_addresses_string = "', '".join(filter(None, mac_addresses))
print(f"IP addresses: '{ip_addresses_string}'")
print(f"MAC addresses: '{mac_addresses_string}'")
print(ip_addresses_string)
print(mac_addresses_string)
