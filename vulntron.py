from library.libraries import *
from tool.intro import *
from tool.port import *
from tool.phone import *
from tool.wifi import *
from vuln.command import open_new_command_line


init(autoreset=True)

# Function to display a loading bar with colors
def show_loading_bar(duration):
    print(Fore.YELLOW + Style.BRIGHT + "Initializing the VULNTRON...")
    # Using tqdm to create a loading bar
    for _ in tqdm(range(duration), desc="Loading", bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt} seconds"):
        time.sleep(1)  # Simulating loading time

    print(Fore.CYAN + "\nInitialization complete!\n")




class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

conf.L3socket = conf.L3socket()



def network_scanner():

    print(Fore.YELLOW + Style.BRIGHT + "Initializing the network scanner...", end="")
    for _ in range(5):
        # Simulate loading with colored dots
        print(Fore.GREEN + ".", end="")
        sys.stdout.flush()
        time.sleep(1)
    print(Fore.CYAN + "\nInitialization complete!\n")




    header_art = r"""
        [-]-----------------------------------------[-]
        _______          __                       __       
        \      \   _____/  |___  _  _____________|  | __   
        /   |   \_/ __ \   __\ \/ \/ /  _ \_  __ \  |/ /   
       /    |    \  ___/|  |  \     (  <_> )  | \/    <    
       \____|__  /\___  >__|   \/\_/ \____/|__|  |__|_ \   
               \/     \/                              \/   
        _________                                         
        /   _____/ ____ _____    ____   ____   ___________ 
        \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __ \
        /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
        /_______  /\___  >____  /___|  /___|  /\___  >__|   
                \/     \/     \/     \/     \/     \/       
        [-]-----------------------------------------[-] """
    
    print(bcolors.RED + header_art)

    print(" ")

   

    while True:
        print(" ")
        print(bcolors.RED + '['+bcolors.YELLOW+'::' + bcolors.RED + ']' + bcolors.GREEN + '  Select What You Want To Do  ' + bcolors.RED + '['+bcolors.YELLOW+'::' + bcolors.RED + ']')
        print(" ")
        print(bcolors.RED + '['+bcolors.YELLOW+'01' + bcolors.RED + ']' + bcolors.GREEN + '  Port_scanner ' + bcolors.RESET )
        print(bcolors.RED + '['+bcolors.YELLOW+'02' + bcolors.RED + ']' + bcolors.GREEN + '  PhoneSphere ' + bcolors.RESET )
        print(bcolors.RED + '['+bcolors.YELLOW+'03' + bcolors.RED + ']' + bcolors.GREEN + '  WiFiWhisperer ' + bcolors.RESET )
        choice = input(Fore.YELLOW + "Enter your choice or 'q' to quit: ")
        if choice == '1':
            port_scanner()
        elif choice == '2':
            phone_number = input("Enter a phone number: ")
            get_phone_info(phone_number)
        elif choice == '3':
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

        elif choice.lower() == 'q':
            print("Stopping the tool....")
            break;  # This will stop the listener thread1
        else:
            print(Fore.RED + "Invalid choice, please try again.")


  

def Vulnerablity_scanner():
    print(Fore.YELLOW + Style.BRIGHT + "Initializing the Vulnerability Scanner...", end="")
    for _ in range(5):
        # Simulate loading with colored dots
        print(Fore.GREEN + ".", end="")
        sys.stdout.flush()
        time.sleep(1)
    print(Fore.CYAN + "\nInitialization complete!\n")

    header_art = r"""
          ,;~;,                                                     |   |   |
                /\_                                                 |   |___|
               (  /                                                 |___|   |
               (()      //)      [::]vulnerability Scanner[::]      |   |   |
               | \\  ,,;;'\                                         |   |___|
           __ _(  )m=(((((((((((((================--------          |___|   |
         /'  ' '()/~' '.(, |                                        |   |   |
      ,;(      )||     |  ~                                         |   |___| 
     ,;' \    /-(.;,   )                                            |___|   |
          ) /       ) /                                             |   |   |
         //         ||  version 1.0                                 |   |___|
        )_\         )_\                                             |   |   |
    """
    
    print(bcolors.GREEN + header_art)
    print(" ")

    while True:
        print(" ")
        print(bcolors.RED + '['+bcolors.YELLOW+'::' + bcolors.RED + ']' + bcolors.GREEN + '  Select What You Want To Do  ' + bcolors.RED + '['+bcolors.YELLOW+'::' + bcolors.RED + ']')
        print(" ")
        print(bcolors.RED + '['+bcolors.YELLOW+'01' + bcolors.RED + ']' + bcolors.GREEN + '  XSS_Scanner ' + bcolors.RESET)
        print(bcolors.RED + '['+bcolors.YELLOW+'02' + bcolors.RED + ']' + bcolors.GREEN + '  SQL_Injection' + bcolors.RESET)
        print(bcolors.RED + '['+bcolors.YELLOW+'03' + bcolors.RED + ']' + bcolors.GREEN + '  CVE_Scanner ' + bcolors.RESET)
        choice = input(Fore.YELLOW + "Enter your choice or 'q' to quit: ")
        print(" ")
        if choice == '1':
            print("Use the command python xsscon.py to start the scanner")
            print(Fore.YELLOW + Style.BRIGHT + "Initializing the Xss Scanner...", end="")
            for _ in range(5):
        # Simulate loading with colored dots
                print(Fore.GREEN + ".", end="")
                sys.stdout.flush()
                time.sleep(1)
            print(Fore.CYAN + "\nInitialization complete!\n")
            open_new_command_line()  # Opens a new command line window
        elif choice == '2':
            print("SQL Injection module in progress...")

        elif choice == '3':
            print("CVE Scanner module in progress...")

        elif choice.lower() == 'q':
            print("Stopping the tool....")
            break

        else:
            print(Fore.RED + "Invalid choice, please try again.")
 







def main_menu():
    while True:
        choice = input(Fore.YELLOW + "Enter your choice or 'q' to quit: ")
        if choice == '1':
            network_scanner()
        elif choice == '2':
            Vulnerablity_scanner()
        elif choice == '3':
            print("working on it.....")
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")


show_loading_bar(3)  # 3 seconds of loading time

# Call the function to display the colored ASCII art
display_colored_intro()

main_menu() # menu driven

