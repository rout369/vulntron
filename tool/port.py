from library.libraries import *


def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0  # True if port is open, False if closed

def monitor_ports(ip, start_port, end_port, interval):
    print(Fore.YELLOW + f"Scanning ports {start_port} to {end_port} on IP {ip}...")

    try:
        for port in range(start_port, end_port + 1):
            is_open = check_port(ip, port)
            if is_open:
                # Mark open ports in red
                port_status = Fore.RED + "OPEN"
            else:
                # Closed ports will still use green
                port_status = Fore.GREEN + "CLOSED"
            
            print(f"Port {port} on {ip} is {port_status}.")
            time.sleep(interval)

    except KeyboardInterrupt:
        print(Fore.RED + "\nStopping Port monitoring....")
        time.sleep(2)
        print(Fore.CYAN + "\nPort monitoring stopped.")
       

def port_scanner():
    print(Fore.YELLOW + Style.BRIGHT + "Initializing the port scanner...", end="")
    time.sleep(1)
    print(Fore.CYAN + "\nInitialization complete!\n")

    ip_address = input(Fore.CYAN + '['+Fore.YELLOW + Style.BRIGHT + '::' + Fore.CYAN + ']'+ Fore.RED + " Enter the IP address to check: ")
    port_range = input(Fore.CYAN + '['+Fore.YELLOW + Style.BRIGHT + '::' + Fore.CYAN + ']'+ Fore.RED + " Enter the port range to check (e.g., 20-80): ")

    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        print(Fore.RED + "Invalid port range. Please enter a range like '20-80'.")
        return

    interval = int(input(Fore.CYAN + '['+Fore.YELLOW + Style.BRIGHT +'::' + Fore.CYAN + ']' + Fore.RED + " Enter the scan interval in seconds: "))

    # Start monitoring the port range
    monitor_ports(ip_address, start_port, end_port, interval)
