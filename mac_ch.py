import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help= "[+] Interface change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help= "[+] new MAC address")

(options, arguments)=parser.parse_args()

inter = options.interface
new_mac = options.new_mac
print("[+]" + inter + " is going to change with  " + new_mac)
subprocess.call(["ifconfig", inter, "down"])
subprocess.call(["ifconfig", inter, "hw","ether",new_mac])
subprocess.call(["ifconfig", inter, "up"])


