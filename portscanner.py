import socket
import termcolor


def scan(target,ports):
	print("\n" + "Scanning Start For " + str(target))
	for port in range(1,ports):
		scan_port(target,port)
def scan_port(ip, port):
	try:
		sock = socket.socket()
		sock.connect((ip,port))
		print(termcolor.colored("[+] Port opened " +str(port), "green" ))
		sock.close()
	except:
		pass

targets = input("[*] Enter the ipaddress( put , in between for multiple ip's): ")
ports = int(input("[*] Enter the number of ports : "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_add in targets.split(','):
		scan(ip_add.strip(' '),ports)
else:
	scan(targets,ports)
