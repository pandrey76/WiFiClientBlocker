import netifaces
# import os
from getmac import get_mac_address
import webbrowser

gws = netifaces.gateways()
print(gws)
print("Router IP: ", gws['default'][netifaces.AF_INET][0])

addrs = netifaces.ifaddresses(gws['default'][netifaces.AF_INET][1])

print("Current device MAC address: ", addrs[netifaces.AF_LINK][0]['addr'])

# import os
# myPipe = os.popen("/sbin/ifconfig","r")
# print(myPipe.read())

# print(os.system('arp -n ' + str(gws['default'][netifaces.AF_INET][0])))

# import re
# import subprocess
# arp_out =subprocess.check_output(['arp','-lan'])
#

# re.findall(r"((\w{2,2}\:{0,1}){6})",arp_out)


# eth_mac = get_mac_address(interface="eth0")
# win_mac = get_mac_address(interface="Ethernet 3")
# ip_mac = get_mac_address(ip="192.168.0.1")
ip_mac = get_mac_address(ip=gws['default'][netifaces.AF_INET][0])
print("Router Mac address: ", ip_mac)



# webbrowser.open('http://net-informations.com', new=0)

# Running default web brouser
webbrowser.open_new('http://net-informations.com')
print(webbrowser.get())
