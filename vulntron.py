import argparse
from library.libraries import *
from tool.intro import *
from tool.port import *
from tool.wifi import *
from vuln.command import open_new_command_line
import threading


def show_loading_bar(duration, spinner_style='dots', spinner_color=Fore.MAGENTA, bar_color=Fore.GREEN):
    print(Fore.YELLOW + Style.BRIGHT + "Initializing the VULNTRON..." + Fore.RESET)

    # Use alive-progress for the loading bar with dynamic color formatting
    with alive_bar(duration, bar='classic', spinner=spinner_style, title="Loading") as bar:
        for _ in range(duration):
            time.sleep(1)  # Simulating loading time
            
            # Print the spinner color, progress bar will follow in the next step
            bar.text = f"{spinner_color}Loading {bar_color}"  # Custom text for spinner and bar colors
            bar()  # Update the bar progress

    print(Fore.CYAN + "\nInitialization complete!\n" + Fore.RESET)

conf.L3socket = conf.L3socket()

def run_nikto(target_url):
    nikto_path = r'C:\Users\acer\nikto-master\program'  # Update this path to your Nikto installation
    os.chdir(nikto_path)
    
    command = ['perl', 'nikto.pl', '-h', target_url]

    print(Fore.YELLOW + "Scanning in progress. Press Ctrl+C to stop..." + Fore.RESET)

    output = []
    
    def run_command():
        try:
            # Capture the output in real-time
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in iter(process.stdout.readline, ''):
                output.append(line)
                print(line, end='')  # Print each line as it's received
            process.stdout.close()
            process.wait()
        except Exception as e:
            print(Fore.RED + f"Error running Nikto: {e}" + Fore.RESET)

    # Start the thread to run the Nikto command
    thread = threading.Thread(target=run_command)
    thread.start()

    try:
        while thread.is_alive():
            # Use alive-progress for the loading animation
            with alive_bar(bar='classic', title='Scanning', spinner='waves') as bar:
                while thread.is_alive():
                    bar()  # Keep the bar moving
                    time.sleep(0.5)  # Sleep for a short period to avoid busy-waiting
        thread.join()  # Wait for the thread to finish
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nScan interrupted. Here is the output gathered so far:\n" + Fore.RESET)
        for line in output:
            print(line, end='')  # Print any output collected before the interruption
        print(Fore.CYAN + "\nScan completed!" + Fore.RESET)

    print(Fore.GREEN + "Nikto Scan Output:\n" + Fore.RESET + ''.join(output))


def display_help():
    show_loading_bar(6, spinner_style='waves', spinner_color=Fore.RED, bar_color=Fore.GREEN)
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
        --nikto             Run Nikto against a target URL.
        --help-info         Display this help information.
    """
    print(Fore.YELLOW + help_text+Fore.RESET)

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
    parser.add_argument('--nikto', action='store_true', help="Run Nikto against a target URL.")
    parser.add_argument('--target', type=str, help="Target URL for Nikto.")
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
    if args.nikto and args.target:
        run_nikto(args.target)
    else:
        print(Fore.RED + "Error: Please specify a target URL for Nikto using --target." + Fore.RESET)




if __name__ == '__main__':
    # show_loading_bar(3)
    main()
