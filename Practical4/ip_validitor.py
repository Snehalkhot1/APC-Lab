import re

ip = input("Enter IP Address: ")

ipv4 = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'

ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

if re.match(ipv4, ip):
    print("Valid IPv4 Address")
elif re.match(ipv6, ip):
    print("Valid IPv6 Address")
else:
    print("Invalid IP Address")