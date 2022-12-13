# Decoy_0.1
this the script that scan the mac adress of the device that connect to the router 

#This scanner runs the arp -a command, which lists the IP and MAC addresses of all devices currently connected to the router. It then uses a regular expression to parse #the output and extract the IP and MAC addresses, which it prints to the screen.

Note that the arp command on Windows may not include the MAC address in the output by default. If this is the case, you can use the -N flag to include the MAC address in #the output, like this: output = subprocess.check_output("arp -a -N", shell=True). You may also need to modify the regular expression to match the specific format of the #output from the arp command on your system.
