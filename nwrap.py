import subprocess as sp
import sys
import os
import ipaddress
from multiprocessing import Manager, Process
from datetime import datetime
import time

THREADS = 5


def atomize_targets(arguments):
    ips = []
    for arg in arguments:    
        if '-' in arg:
            # Handle IP Range format
            base_ip, end = arg.split('-')
            start_ip = ipaddress.IPv4Address(base_ip)
            end_ip = start_ip + int(end.split('.')[-1]) - int(str(start_ip).split('.')[-1])
            for ip_int in range(int(start_ip), int(end_ip) + 1):
                ips.append(str(ipaddress.IPv4Address(ip_int)))
        elif '/' in arg:
            # Handle CIDR Notation
            network = ipaddress.IPv4Network(arg, strict=False)
            for ip in network:
                ips.append(str(ip))
        else:
            # Handle Single IP Address
            ips.append(arg)
    
    sortable_ips = [ipaddress.ip_address(ip) for ip in list(set(ips))]
    sorted_ips = sorted(sortable_ips)
    
    return [str(ip) for ip in sorted_ips]



def start_enumeration(nmap_args, target_list):

    #create base directory
    folder_name = f"nmap_outputs_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}"   

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        print("Could not create output path")
        exit(1)
    
    
    for target in target_list:
        output_path = f"{folder_name}/{target}"
        os.makedirs(output_path)

        command = ["nmap"] + nmap_args.split(" ") + ["-oA", f"{output_path}/{target}", target]

        print(command)
        result = sp.run(command)


def main():
    if len(sys.argv) < 3:
        print("Incorret input!\nnwrap.py \"[NMAP OPTIONS]\" [TARGETS...]")
        exit(1)
    if "-oN" in sys.argv[1] or "-oX" in sys.argv[1] or "-oS" in sys.argv[1] or "-oG" in sys.argv[1] or "-oA" in sys.argv[1]:
        print("Please do not specify any output options for nmap, the script always uses -oA for all targets")
        exit(1)

    target_list = atomize_targets(sys.argv[2:])
    start_enumeration(sys.argv[1], target_list)

if __name__ == '__main__':
    main()
