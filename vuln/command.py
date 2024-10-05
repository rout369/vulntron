import os
import platform
import subprocess

def is_wsl():
    """Check if the current environment is WSL."""
    return 'microsoft' in platform.uname().release.lower()

def open_new_command_line():
    current_os = platform.system()
    current_dir = os.getcwd()  # Get the current working directory

    if current_os == "Windows":
        # Open new cmd in the current directory
        subprocess.Popen(f'start cmd /K "cd {current_dir}"', shell=True)
    elif is_wsl():
        # Open a new WSL terminal in the current directory
        subprocess.Popen(f'cmd.exe /C start wsl --cd {current_dir}', shell=True)
    elif current_os == "Linux":
        # Open gnome-terminal or xterm in the current directory (if available)
        try:
            subprocess.Popen(['gnome-terminal', '--working-directory', current_dir])
        except FileNotFoundError:
            # Fallback to xterm if gnome-terminal is not available
            subprocess.Popen(['xterm', '-e', f'cd {current_dir} && bash'])
    elif current_os == "Darwin":  # macOS
        # Open Terminal in the current directory
        subprocess.Popen(['open', '-a', 'Terminal', current_dir])
