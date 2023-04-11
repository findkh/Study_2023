import uuid 

# 이더넷 맥주소 

def get_mac_address():    
    mac_hex = uuid.getnode()
    mac = '-'.join(("%012X" % mac_hex)[i:i+2] for i in range(0, 12, 2))
    return mac

print("MAC Address: ", get_mac_address())