from library.libraries import *

def get_connected_wifi_details():
    try:
        # Run the command to get Wi-Fi information (Windows specific)
        command = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        
        # Check if the command executed successfully
        if command.returncode != 0:
            print(Fore.RED + "Failed to retrieve Wi-Fi information.")
            return None

        # Output of the command
        output = command.stdout
        print(Fore.CYAN + "Command output:\n" + output)  # Debugging step to check the output

        # Extract the SSID (Wi-Fi name) using regex
        ssid_match = re.search(r"SSID\s*:\s*(.+)", output)
        if ssid_match:
            ssid = ssid_match.group(1).strip()
        else:
            print(Fore.RED + "Could not find the SSID. Are you connected to a Wi-Fi network?")
            return None

        # Extract the MAC address of the Wi-Fi adapter using regex
        mac_match = re.search(r"BSSID\s*:\s*(.+)", output)
        mac_address = mac_match.group(1).strip() if mac_match else "N/A"

        # Extract the signal strength using regex
        signal_match = re.search(r"Signal\s*:\s*(\d+)%", output)
        signal_strength = signal_match.group(1).strip() if signal_match else "N/A"
        
        # Extract the radio type (e.g., 802.11n, 802.11ac) using regex
        radio_type_match = re.search(r"Radio type\s*:\s*(.+)", output)
        radio_type = radio_type_match.group(1).strip() if radio_type_match else "N/A"
        
        # Extract authentication and cipher details using regex
        auth_match = re.search(r"Authentication\s*:\s*(.+)", output)
        cipher_match = re.search(r"Cipher\s*:\s*(.+)", output)
        
        authentication = auth_match.group(1).strip() if auth_match else "N/A"
        cipher = cipher_match.group(1).strip() if cipher_match else "N/A"

        # Run the command to get IP configuration information
        ip_command = subprocess.run(["ipconfig"], capture_output=True, text=True)
        ip_output = ip_command.stdout
        
        # Extract the internal IP (IPv4 address)
        ip_match = re.search(r"IPv4 Address[\.\s]*:\s*(.+)", ip_output)
        if ip_match:
            ip_address = ip_match.group(1).strip()
        else:
            ip_address = "N/A"

        # Extract the default gateway (internal IP of the mobile device)
        gateway_match = re.search(r"Default Gateway[\.\s]*:\s*(\d+\.\d+\.\d+\.\d+)", ip_output)
        if gateway_match:
            gateway_ip = gateway_match.group(1).strip()
        else:
            gateway_ip = "N/A"

        # Fetch the external IP (public IP) of the mobile device
        external_ip = requests.get('https://api.ipify.org').text

        # Fetch the router's IP address using a traceroute command (getting the second hop in the route)
        router_ip_command = subprocess.run(["tracert", "-h", "2", "8.8.8.8"], capture_output=True, text=True)
        router_ip_output = router_ip_command.stdout
        router_ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", router_ip_output.splitlines()[2])  # Second hop in the trace
        router_ip = router_ip_match.group(1).strip() if router_ip_match else "N/A"

        # Print the details of the connected Wi-Fi network in colored output
        print(Fore.YELLOW + Style.BRIGHT + f"\nConnected to Wi-Fi network: {Fore.CYAN + ssid}")
        print(Fore.YELLOW + Style.BRIGHT + f"MAC Address: {Fore.CYAN + mac_address}")
        print(Fore.YELLOW + Style.BRIGHT + f"Device IP Address (Your device): {Fore.CYAN + ip_address}")
        print(Fore.YELLOW + Style.BRIGHT + f"Router (Mobile Device) Internal IP Address: {Fore.CYAN + gateway_ip}")
        print(Fore.YELLOW + Style.BRIGHT + f"Router (Mobile Device) External/Public IP Address: {Fore.CYAN + external_ip}")
        print(Fore.YELLOW + Style.BRIGHT + f"Router IP Address (via Traceroute): {Fore.CYAN + router_ip}")
        print(Fore.YELLOW + Style.BRIGHT + f"Signal Strength: {Fore.CYAN + signal_strength + '%'}")
        print(Fore.YELLOW + Style.BRIGHT + f"Radio Type: {Fore.CYAN + radio_type}")
        print(Fore.YELLOW + Style.BRIGHT + f"Authentication: {Fore.CYAN + authentication}")
        print(Fore.YELLOW + Style.BRIGHT + f"Cipher: {Fore.CYAN + cipher}")

        # Return the details as a dictionary
        return {
            "SSID": ssid,
            "MAC Address": mac_address,
            "Device IP Address": ip_address,
            "Router Internal IP Address": gateway_ip,
            "Router External/Public IP Address": external_ip,
            "Router IP Address (Traceroute)": router_ip,
            "Signal Strength": signal_strength,
            "Radio Type": radio_type,
            "Authentication": authentication,
            "Cipher": cipher
        }

    except Exception as e:
        print(Fore.RED + f"Error occurred: {e}")
        return None
