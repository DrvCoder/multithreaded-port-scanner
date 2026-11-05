#!/usr/bin/env python3
import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    """
    Attempts to establish a TCP connection to a specific port on the target IP.
    Returns the port number if open, otherwise None.
    """
    try:
        # Create an IPv4 TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0) # 1 second timeout
            result = s.connect_ex((target_ip, port))
            if result == 0:
                return port
    except socket.gaierror:
        print("\n[-] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\n[-] Could not connect to server.")
        sys.exit()
    return None

def main():
    # Target specification (defaulting to localhost/safe target if none provided)
    target_input = input("Enter target IP or domain (default: 127.0.0.1): ").strip()
    target = target_input if target_input else "127.0.0.1"

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[-] Error: Hostname '{target}' could not be resolved.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

    # Define standard port range (e.g., 1 to 1024)
    ports = range(1, 1025)
    open_ports = []

    # Using ThreadPoolExecutor for concurrent multi-threaded execution
    print("[*] Scanning ports using multi-threading...")
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            # Map the port scan function across the port range
            futures = {executor.submit(scan_port, target_ip, port): port for port in ports}
            
            for future in futures:
                port = futures[future]
                try:
                    open_port = future.result()
                    if open_port:
                        print(f"[+] Port {open_port} is OPEN")
                        open_ports.append(open_port)
                except Exception as e:
                    pass

    except KeyboardInterrupt:
        print("\n[!] Exiting script user interruption.")
        sys.exit()

    print("-" * 50)
    print(f"Scan completed at {str(datetime.now())}")
    print(f"Total open ports found: {len(open_ports)}")
    print("-" * 50)

if __name__ == "__main__":
    main()