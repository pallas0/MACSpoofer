import subprocess
import re
import optparse

#get options for program for interface and new mac address
#change the mac address
#check mac address with new mac adress

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter an interface")
    parser.add_option("-m","--mac", help="Enter New MAC address")
    (options, args) = parser.parse_args()

    return options

def mac_spoof(interface, mac_add):
    print("[+] Disconnecting "+ interface)
    subprocess.run(["ifconfig", interface, "down"])
    print("[+] Spoofing MAC address...")
    subprocess.run(["ifconfig", interface, "hw", "ether", mac_add])
    print("[+] Reconnecting " + interface)
    subprocess.run(["ifconfig", interface, "up"])

# def mac_check(interface):
#     ifconfig = re.search()