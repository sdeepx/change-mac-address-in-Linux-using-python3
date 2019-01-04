import subprocess
import optparse

def mac_change(interface, new_mac):
    print("[+] Your MAC address changed for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "[+] Interface changes it's mac address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "[+] new MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use '-h' or '--help' for more info")
    if not options.new_mac:
        parser.error("[-] please specify a mac, use '-h' or '--help' for more info")
    return options

options = get_args()
mac_change(options.interface, options.new_mac)
