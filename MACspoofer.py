import subprocess
import re
import optparse

#get options for program for interface and new mac address
#change the mac address
#check mac address with new mac adress

#debugging notes:
#   specify 'en0' in place of 'wlan0' for interface - this isn't linux
#

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter an interface")
    parser.add_option("-m","--mac", dest="new_mac", help="Enter New MAC address")
    (options, args) = parser.parse_args()

    print(options)
    return options

def mac_spoof(interface, mac_add):
    print("[+] Disconnecting "+ interface)
    subprocess.run(["ifconfig", interface, "down"])
    print("[+] Spoofing MAC address...")
    subprocess.run(["ifconfig", interface, "ether", mac_add])
    print("[+] Reconnecting " + interface)
    subprocess.run(["ifconfig", interface, "up"])

def mac_check(interface):
    # checking ifconfig interface for validity (like lo interfaces etc...)
    #options = get_options()
    ifconfig = subprocess.check_output(["ifconfig", options.interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if current_mac.group(0) == options.new_mac:
        return current_mac.group(0)
    else:
        print("[-] Error reading MAC address")


options = get_options()

print("[+] "+options.interface+" MAC address :"+ str(mac_check(options.interface)))

mac_spoof(options.interface, options.new_mac)

if mac_check(options.interface) == options.new_mac:
    print("[+] ", options.interface + " MAC address has been spoofed")
else:
    print("[-] "+ options.interface + " MAC address Spoofing has failed =(")