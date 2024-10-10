import argparse
from library.libraries import *
from tool.intro import *
from tool.port import *
from tool.wifi import *
from vuln.command import open_new_command_line


def display_help():
    display_colored_intro()
    print("")
    help_text = """
    Usage: python Vulntron.py [OPTIONS]

    Vulntron: A comprehensive ethical hacking tool for vulnerability analysis.

    Options:
        --show-intro,       Display the tool description.
        --port-scanner, -Ps Launch the port scanner.
        --wifi, -W          Launch the Wi-Fi Information Gathering tool.
        --Xss               Launch New command line for XssScanner.
        --Sql               Launch New command line for SQLScanner.
        --help-info         Display this help information.
    """
    print(Fore.YELLOW + help_text)

def main():
    # Argument parser for command-line options
    parser = argparse.ArgumentParser(description='Vulntron: A comprehensive ethical hacking tool for vulnerability analysis')
    
    # Add an argument for showing the colored intro
    parser.add_argument('--show-intro',action='store_true',help="Display the tool description.")
    # parser.add_argument('--show-description', action='store_true', help='Display the tool description')
    parser.add_argument('--port-scanner','-Ps', action='store_true', help="Launch the port scanner.")
    parser.add_argument('--wifi','-W', action='store_true', help="Launch the WI-Fi Information Gathering tool.")
    parser.add_argument('--Xss', action='store_true', help="Launch New command line for XssScanner.")
    parser.add_argument('--Sql', action='store_true', help="Launch New command line for SQLScanner.")
    parser.add_argument('--help-info', action='store_true', help="Display help information about command-line options.")
    args = parser.parse_args()

    # If the user passes the --show-intro flag, show the intro
    if args.help_info:
        display_help()
    if args.show_intro:
        display_colored_intro()
    if args.port_scanner:
        network_scanner()
        port_scanner()
    if args.wifi:
        wifi()
        print(Fore.YELLOW + Style.BRIGHT + "Gathering _Wifi_Information...", end="")
        for _ in range(5):
            print(Fore.GREEN + ".", end="")
            sys.stdout.flush()
            time.sleep(1)
        wifi_info = get_connected_wifi_details()
        if wifi_info:
            print(Fore.GREEN + "\nWi-Fi Information:")
            for key, value in wifi_info.items():
                print(Fore.YELLOW + f"{key}: {Fore.CYAN + value}")       
    if args.Xss:
        Vulnerablity_scanner()
        print("Use the command python xssxplore.py to start the scanner")
        print(Fore.YELLOW + Style.BRIGHT + "Initializing the Xss Scanner...", end="")
        for _ in range(5):
        # Simulate loading with colored dots
                print(Fore.GREEN + ".", end="")
                sys.stdout.flush()
                time.sleep(1)
        print(Fore.CYAN + "\nInitialization complete!\n")
        open_new_command_line()
    if args.Sql:
        Vulnerablity_scanner()
        print("Use the command python inject.py --help to start the scanner")
        print(Fore.YELLOW + Style.BRIGHT + "Initializing Sql Injection Scanner...", end="")
        for _ in range(5):
        # Simulate loading with colored dots
                print(Fore.GREEN + ".", end="")
                sys.stdout.flush()
                time.sleep(1)
        print(Fore.CYAN + "\nInitialization complete!\n")
        open_new_command_line()
           
if __name__ == '__main__':
    main()
