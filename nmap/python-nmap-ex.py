import nmap

nm = nmap.PortScanner()

sc = nm.scan("127.0.0.1", "22-443")
print(sc)
print(nm.command_line())
print(nm.scaninfo())
print(nm.all_hosts())
