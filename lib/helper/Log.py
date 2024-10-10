from lib.helper.helper import * 
import sys

class Log:
    
    # ANSI color codes
    Y = "\033[1;33m"  # Yellow
    G = "\033[1;32m"  # Green
    R = "\033[1;31m"  # Red
    M = "\033[1;35m"  # Magenta
    N = "\033[0m"     # Reset

    # Emojis for different log levels
    EMOJIS = {
        "INFO": "ℹ️",
        "WARNING": "⚠️",
        "CRITICAL": "🚨"
    }

    # Terminal prompt representation with magenta color
    PROMPT = f"{M}┌──(XssXplore 🕵️‍♂️SCANNER)-[㉿]\n└─$-o> {N}"

    @classmethod
    def _format_message(cls, level, text):
        emoji = cls.EMOJIS.get(level, "")
        color = cls.G if level == "INFO" else (cls.Y if level == "WARNING" else cls.R)
        return f"{cls.PROMPT} {emoji} {color}{level}:{cls.N} {text}"

    @classmethod
    def info(cls, text):
        print(cls._format_message("INFO", text))

    @classmethod
    def warning(cls, text):
        print(cls._format_message("WARNING", text))

    @classmethod
    def high(cls, text):
        print(cls._format_message("CRITICAL", text))

    @classmethod
    def set_terminal_style(cls):
        print(f"{cls.M}┌──(XssXplore📡Log){cls.N}")
        print(f"{cls.M}└──#-o>{cls.N}",Log.info("Connection established successfully!"))

# # Usage
Log.set_terminal_style()
# Log.info("Connection established successfully!")
# Log.warning("Potential XSS vulnerability detected at https://example.com/vulnerable")
# Log.high("Detected XSS (GET) at https://example.com/attack")
