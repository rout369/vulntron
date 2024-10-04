from lib.helper.helper import * 
from datetime import datetime

# Color codes for console output
Y = "\033[93m"  # Yellow
G = "\033[92m"  # Green
R = "\033[91m"  # Red
N = "\033[0m"   # Reset

class Log:

    @classmethod
    def info(cls, text):
        print("[" + Y + datetime.now().strftime("%H:%M:%S") + N + "] [" +"ℹ️"+ G + "INFO" + N + "] " + text)

    @classmethod
    def warning(cls, text):
        print("[" + Y + datetime.now().strftime("%H:%M:%S") + N + "] ["  +"⚠️" + Y + "WARNING" + N + "] " + text)

    @classmethod
    def high(cls, text):
        print("[" + Y + datetime.now().strftime("%H:%M:%S") + N + "] ["  +"🚨" + R + "CRITICAL" + N + "] " + text)
