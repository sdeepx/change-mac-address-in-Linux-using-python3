import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "[+] Interface change it's mac address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "[+] new Mac address")
    return parser.parse_args()

def mac_change(interface, new_mac):
    print("[+] your MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_argument()
mac_change(options.interface, options.new_mac)
