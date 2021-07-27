import traceback
from socket import socket, AF_INET, SOCK_STREAM, \
                   gethostbyaddr, gethostbyname, setdefaulttimeout

def con_scan(tgt_host: str, tgt_port: int) -> bool:
    setdefaulttimeout(1)
    connskt = socket(AF_INET, SOCK_STREAM)
    try:
        connskt.connect((tgt_host, tgt_port))
        print(f'[+]{tgt_port}/tcp open')
        connskt.close()
        return True
    except Exception as e:
        if str(e) == 'timed out':  # only catching timeout problems
            print(f'[-]{tgt_port}/tcp closed')
        else: # any other error (types, etc.) are printed 
            traceback.print_exc()
        return False
        
def port_scan(tgt_host: str, tgt_ports: list[int]):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except Exception:
        traceback.print_exc()
        print(f'[-] Cannot resolve {tgt_host}')
        return

    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print(f'\n[+] Scan result of: {tgt_name[0]}')
    except Exception:
        print(f'\n[+] Scan result of: {tgt_ip}')
    for tgt_port in tgt_ports:
        print(f'Scanning Port: {str(tgt_port)}')
        con_scan(tgt_host, int(tgt_port))


if __name__ == '__main__':
    # con_scan('216.58.207.238', 22)
    port_scan('google.com', [80,22,100,8080,40])
