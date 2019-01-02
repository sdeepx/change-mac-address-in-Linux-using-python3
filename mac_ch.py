import subprocess
import optparse

def mac_change(interface, new_mac):
    print("[+] Your " + interface + " is going to change with " + new_mac)

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "[+] Interface change it's MAC address")
parser.add_option("-m", "--mac", dest = "new_mac", help = "[+] new MAC address")
(options, arguments) = parser.parse_args()

mac_change(options.interface, options.new_mac)
