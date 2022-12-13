import subprocess
import re

# Run the "arp -a" command to get a list of IP addresses and MAC addresses
output = subprocess.check_output("arp -a", shell=True)

# Use a regular expression to parse the output and extract the IP and MAC addresses
pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b.*?([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"
matches = re.findall(pattern, output)

# Print the IP and MAC addresses
for match in matches:
    ip = match[0]
    mac = match[1]
    print(f"IP: {ip} MAC: {mac}")