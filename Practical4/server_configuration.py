server_ip = ("192.168.1.10",)
allowed_ips = ["192.168.1.20", "192.168.1.21"]

def update_allowed_ips():
    ip = input("Enter new allowed IP: ")
    allowed_ips.append(ip)
    print("Allowed IP updated.")

def update_server_ip():
    try:
        server_ip[0] = input("Enter new server IP: ")
    except TypeError:
        print("Server IP cannot be changed because it is stored in a tuple.")

update_allowed_ips()
update_server_ip()

print("\nServer IP:", server_ip)
print("Allowed IPs:", allowed_ips)